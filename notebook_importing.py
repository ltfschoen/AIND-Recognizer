import logging
"""
Module directly collated from reading the following instructions and copy/paste code
from the Gist. When imported into say `solution.py`, it calls
the NotebookFinder class, which searches all .ipynb files in the
current directory and then for each Jupyter notebook that it finds
it uses a NotebookLoader class, which by default finds and loads
all cells that are of the cell type 'code' so that functions
in those cells may be called and run. The code in the Gist has been
modified so as not to run all code cells, but only those that
contain the following first 13 characters `###_DEBUG_IDE`, and then
simply added those characters to the start of any Jupyter Notebook
Code Cells that I wanted to be loaded.

References:
http://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Importing%20Notebooks.html
https://gist.github.com/DCAL12/1a872bd63bedfb7b12612c8a7ec0f52e
"""
import io, os, sys, types
from IPython import get_ipython
from nbformat import read
from IPython.core.interactiveshell import InteractiveShell

def find_notebook(fullname, path=None):
    """find a notebook, given its fully qualified name and an optional path
    This turns "foo.bar" into "foo/bar.ipynb"
    and tries turning "Foo_Bar" into "Foo Bar" if Foo_Bar
    does not exist.
    """
    name = fullname.rsplit('.', 1)[-1]
    if not path:
        path = ['']
    for d in path:
        nb_path = os.path.join(d, name + ".ipynb")
        if os.path.isfile(nb_path):
            return nb_path
        # let import Notebook_Name find "Notebook Name.ipynb"
        nb_path = nb_path.replace("_", " ")
        if os.path.isfile(nb_path):
            return nb_path

class NotebookLoader(object):
    """Module Loader for Jupyter Notebooks"""
    def __init__(self, path=None):
        self.shell = InteractiveShell.instance()
        self.path = path

    def load_module(self, fullname):
        """import a notebook as a module"""
        path = find_notebook(fullname, self.path)

        logging.debug("Importing Jupyter notebook from %s" % path)

        # load the notebook object
        with io.open(path, 'r', encoding='utf-8') as f:
            nb = read(f, 4)

        # create the module and add it to sys.modules
        # if name in sys.modules:
        #    return sys.modules[name]
        mod = types.ModuleType(fullname)
        mod.__file__ = path
        mod.__loader__ = self
        mod.__dict__['get_ipython'] = get_ipython
        sys.modules[fullname] = mod

        # extra work to ensure that magics that would affect the user_ns
        # actually affect the notebook module's ns
        save_user_ns = self.shell.user_ns
        self.shell.user_ns = mod.__dict__

        try:
            logging.debug("Searching for Code Cells within the Jupyter Notebook marked with first characters '###_DEBUG_IDE' ")
            for cell in nb.cells:
                if cell.cell_type == 'code' and cell.source[:13] == '###_DEBUG_IDE':
                    # transform the input to executable Python
                    code = self.shell.input_transformer_manager.transform_cell(cell.source)
                    # run the code in themodule
                    exec(code, mod.__dict__)
        finally:
            self.shell.user_ns = save_user_ns
        return mod

class NotebookFinder(object):
    """Module finder that locates Jupyter Notebooks"""
    def __init__(self):
        self.loaders = {}

    def find_module(self, fullname, path=None):
        nb_path = find_notebook(fullname, path)
        if not nb_path:
            return

        key = path
        if path:
            # lists aren't hashable
            key = os.path.sep.join(path)

        if key not in self.loaders:
            self.loaders[key] = NotebookLoader(path)
        return self.loaders[key]

## Aside: displaying notebooks
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

from IPython.display import display, HTML

formatter = HtmlFormatter()
lexer = PythonLexer()

# publish the CSS for pygments highlighting
display(HTML("""
<style type='text/css'>
%s
</style>
""" % formatter.get_style_defs()
             ))

def show_notebook(fname):
    """display a short summary of the cells of a notebook"""
    with io.open(fname, 'r', encoding='utf-8') as f:
        nb = read(f, 4)
    html = []
    for cell in nb.cells:
        html.append("<h4>%s cell</h4>" % cell.cell_type)
        if cell.cell_type == 'code':
            html.append(highlight(cell.source, lexer, formatter))
        else:
            html.append("<pre>%s</pre>" % cell.source)
    display(HTML('\n'.join(html)))

# logging.info("Showing summary of Jupyter Notebook cells")
# show_notebook(os.path.join("", "asl_recognizer.ipynb"))

# Now we register the NotebookFinder with sys.meta_path
sys.meta_path.append(NotebookFinder())