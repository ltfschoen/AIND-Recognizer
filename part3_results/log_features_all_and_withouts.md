/Library/Frameworks/Python.framework/Versions/3.6/bin/python3.6 "~/Library/Application Support/IntelliJIdea2016.3/python/helpers/pydev/pydev_run_in_console.py" 59625 59626 ~/code/aind-projects/AIND-Recognizer/main.py
Python 3.6.0 (v3.6.0:41df79263a11, Dec 22 2016, 17:23:13)
Type "copyright", "credits" or "license" for more information.
IPython 5.3.0 -- An enhanced Interactive Python.
?         -> Introduction and overview of IPython's features.
%quickref -> Quick reference.
help      -> Python's own help system.
object?   -> Details about 'object', use 'object??' for extra details.
PyDev console: using IPython 5.3.0
Running ~/code/aind-projects/AIND-Recognizer/main.py
Backend MacOSX is interactive backend. Turning interactive mode on.
'19/04/2017 04:03:16 PM' - root - INFO - Starting Recogniser
'19/04/2017 04:03:16 PM' - root - DEBUG - Registering hooks so Jupyter Notebooks .ipynb importable
<IPython.core.display.HTML object>
'19/04/2017 04:03:16 PM' - root - DEBUG - Importing Jupyter notebook from asl_recognizer.ipynb
'19/04/2017 04:03:16 PM' - traitlets - ERROR - Notebook JSON is invalid: 'execution_count' is a required property
Failed validating 'required' in execute_result:
On instance['cells'][24]['outputs'][1]:
{'data': {'text/html': '<div>\n'
                       '<table border="1" class="dataframe">\n'
                       '  <thead>\n'
                       '    <tr sty...',
          'text/plain': '            left-x     left-y    right-x    '
                        'right-y    nose-x   ...'},
 'metadata': {},
 'output_type': 'execute_result'}
'19/04/2017 04:03:16 PM' - root - DEBUG - Searching for Code Cells within the Jupyter Notebook marked with first characters '###_DEBUG_IDE'
Called .ipynb file from .py file using notebook_importing.py
'19/04/2017 04:03:16 PM' - root - DEBUG - MyRecognizer
'19/04/2017 04:03:16 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:03:16 PM' - root - DEBUG - Please wait...
'19/04/2017 04:03:58 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:03:58 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta, right
Chosen Model Selector:  SelectorConstant
Training complete for JOHN with 3 states with time 1.2980010579922237 seconds
Training complete for WRITE with 3 states with time 0.01632259099278599 seconds
Training complete for HOMEWORK with 3 states with time 0.022748936025891453 seconds
Training complete for IX-1P with 3 states with time 0.029094841971527785 seconds
Training complete for SEE with 3 states with time 0.027687057969160378 seconds
Training complete for YESTERDAY with 3 states with time 0.05400504101999104 seconds
Training complete for IX with 3 states with time 0.6851065729861148 seconds
Training complete for LOVE with 3 states with time 0.06380813202122226 seconds
Training complete for MARY with 3 states with time 0.3296887920005247 seconds
Training complete for CAN with 3 states with time 0.09699346701381728 seconds
Training complete for GO with 3 states with time 0.049287909001577646 seconds
Training complete for GO1 with 3 states with time 0.029557225992903113 seconds
Training complete for FUTURE with 3 states with time 0.0943194690044038 seconds
Training complete for GO2 with 3 states with time 0.015859170991461724 seconds
Training complete for PARTY with 3 states with time 0.014764384017325938 seconds
Training complete for FUTURE1 with 3 states with time 0.01787726004840806 seconds
Training complete for HIT with 3 states with time 0.013635603012517095 seconds
Training complete for BLAME with 3 states with time 0.021757894952315837 seconds
Training complete for FRED with 3 states with time 0.015591435949318111 seconds
Training complete for FISH with 3 states with time 0.015207807999104261 seconds
Training complete for WONT with 3 states with time 0.020911043975502253 seconds
Training complete for EAT with 3 states with time 0.021708780026528984 seconds
Training complete for BUT with 3 states with time 0.019959945988375694 seconds
Training complete for CHICKEN with 3 states with time 0.018270136031787843 seconds
Training complete for VEGETABLE with 3 states with time 0.02272625803016126 seconds
Training complete for CHINA with 3 states with time 0.017987716011703014 seconds
Training complete for PEOPLE with 3 states with time 0.019812187005300075 seconds
Training complete for PREFER with 3 states with time 0.024898611998651177 seconds
Training complete for BROCCOLI with 3 states with time 0.03189521504100412 seconds
Training complete for LIKE with 3 states with time 0.042395236028824 seconds
Training complete for LEAVE with 3 states with time 0.02060162101406604 seconds
Training complete for SAY with 3 states with time 0.014218623051419854 seconds
Training complete for BUY with 3 states with time 0.23154551698826253 seconds
Training complete for HOUSE with 3 states with time 0.05212449899408966 seconds
Training complete for KNOW with 3 states with time 0.01781999901868403 seconds
Training complete for CORN with 3 states with time 0.0239228309947066 seconds
Training complete for CORN1 with 3 states with time 0.02041329996427521 seconds
Training complete for THINK with 3 states with time 0.014640055014751852 seconds
Training complete for NOT with 3 states with time 0.03205755102680996 seconds
Training complete for PAST with 3 states with time 0.012766743951942772 seconds
Training complete for LIVE with 3 states with time 0.012507431965786964 seconds
Training complete for CHICAGO with 3 states with time 0.0128022960270755 seconds
Training complete for CAR with 3 states with time 0.06258133699884638 seconds
Training complete for SHOULD with 3 states with time 0.04227733297739178 seconds
Training complete for DECIDE with 3 states with time 0.015516421000938863 seconds
Training complete for VISIT with 3 states with time 0.06261464999988675 seconds
Training complete for MOVIE with 3 states with time 0.018266831000801176 seconds
Training complete for WANT with 3 states with time 0.016328011988662183 seconds
Training complete for SELL with 3 states with time 0.016841822012793273 seconds
Training complete for TOMORROW with 3 states with time 0.013693524990230799 seconds
Training complete for NEXT-WEEK with 3 states with time 0.013182293041609228 seconds
Training complete for NEW-YORK with 3 states with time 0.01598749397089705 seconds
Training complete for LAST-WEEK with 3 states with time 0.015610266011208296 seconds
Training complete for WILL with 3 states with time 0.018535923038143665 seconds
Training complete for FINISH with 3 states with time 0.033419878978747874 seconds
Training complete for ANN with 3 states with time 0.016059525951277465 seconds
Training complete for READ with 3 states with time 0.02092655998421833 seconds
Training complete for BOOK with 3 states with time 0.0737950429902412 seconds
Training complete for CHOCOLATE with 3 states with time 0.023135209979955107 seconds
Training complete for FIND with 3 states with time 0.015173801977653056 seconds
Training complete for SOMETHING-ONE with 3 states with time 0.049221426947042346 seconds
Training complete for POSS with 3 states with time 0.05658426898298785 seconds
Training complete for BROTHER with 3 states with time 0.018532053974922746 seconds
Training complete for ARRIVE with 3 states with time 0.07197614200413227 seconds
Training complete for HERE with 3 states with time 0.018911491963081062 seconds
Training complete for GIVE with 3 states with time 0.05114429397508502 seconds
Training complete for MAN with 3 states with time 0.0337678010109812 seconds
Training complete for NEW with 3 states with time 0.053650434012524784 seconds
Training complete for COAT with 3 states with time 0.01789897301932797 seconds
Training complete for WOMAN with 3 states with time 0.039496555051300675 seconds
Training complete for GIVE1 with 3 states with time 0.05932835297426209 seconds
Training complete for HAVE with 3 states with time 0.041053570981603116 seconds
Training complete for FRANK with 3 states with time 0.023029331990983337 seconds
Training complete for BREAK-DOWN with 3 states with time 0.025720364996232092 seconds
Training complete for SEARCH-FOR with 3 states with time 0.015315698983613402 seconds
Training complete for WHO with 3 states with time 0.2398787169950083 seconds
Training complete for WHAT with 3 states with time 0.15772446402115747 seconds
Training complete for LEG with 3 states with time 0.012951898039318621 seconds
Training complete for FRIEND with 3 states with time 0.014148721005767584 seconds
Training complete for CANDY with 3 states with time 0.013753415958490223 seconds
Training complete for BLUE with 3 states with time 0.023669144022278488 seconds
Training complete for SUE with 3 states with time 0.02639340201858431 seconds
Training complete for BUY1 with 3 states with time 0.03277350700227544 seconds
Training complete for STOLEN with 3 states with time 0.01674645399907604 seconds
Training complete for OLD with 3 states with time 0.013110593019519001 seconds
Training complete for STUDENT with 3 states with time 0.020190313982311636 seconds
Training complete for VIDEOTAPE with 3 states with time 0.02925458998652175 seconds
Training complete for BORROW with 3 states with time 0.015220755012705922 seconds
Training complete for MOTHER with 3 states with time 0.015383346995804459 seconds
Training complete for POTATO with 3 states with time 0.012633566977456212 seconds
Training complete for TELL with 3 states with time 0.022345240984577686 seconds
Training complete for BILL with 3 states with time 0.024601290002465248 seconds
Training complete for THROW with 3 states with time 0.01894280599663034 seconds
Training complete for APPLE with 3 states with time 0.0241001810063608 seconds
Training complete for NAME with 3 states with time 0.01462864299537614 seconds
Training complete for SHOOT with 3 states with time 0.014921739988494664 seconds
Training complete for SAY-1P with 3 states with time 0.012790136970579624 seconds
Training complete for SELF with 3 states with time 0.014769030967727304 seconds
Training complete for GROUP with 3 states with time 0.013311618997249752 seconds
Training complete for JANA with 3 states with time 0.02050343295559287 seconds
Training complete for TOY1 with 3 states with time 0.014043270028196275 seconds
Training complete for MANY with 3 states with time 0.013173924991860986 seconds
Training complete for TOY with 3 states with time 0.013518585998099297 seconds
Training complete for ALL with 3 states with time 0.015605357009917498 seconds
Training complete for BOY with 3 states with time 0.02228723996086046 seconds
Training complete for TEACHER with 3 states with time 0.05602878495119512 seconds
Training complete for GIRL with 3 states with time 0.023822610033676028 seconds
Training complete for BOX with 3 states with time 0.032326363027095795 seconds
Training complete for GIVE2 with 3 states with time 0.015558951999992132 seconds
Training complete for GIVE3 with 3 states with time 0.020343595009762794 seconds
Training complete for GET with 3 states with time 0.013162585033569485 seconds
Training complete for PUTASIDE with 3 states with time 0.013507006980944425 seconds
Number of word models returned = 112
'19/04/2017 04:04:15 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:04:15 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:04:25 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5617977528089888
Total correct: 78 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: *POSS WRITE HOMEWORK                                          JOHN WRITE HOMEWORK
    7: JOHN *PEOPLE *HAVE *ARRIVE                                    JOHN CAN GO CAN
   12: JOHN *HAVE *WHAT CAN                                          JOHN CAN GO CAN
   21: JOHN *NEW *SOMETHING-ONE *MARY *CAR *CAR *VISIT *WHO          JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN LIKE IX *LIKE IX                                         JOHN LIKE IX IX IX
   28: JOHN *WHO IX *LIKE IX                                         JOHN LIKE IX IX IX
   30: JOHN LIKE *MARY *MARY *MARY                                   JOHN LIKE IX IX IX
   36: MARY *PREFER *IX *GIVE *IX *MARY                              MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN *MARY *CORN MARY *MARY                                   JOHN IX THINK MARY LOVE
   43: *FRANK *POSS BUY HOUSE                                        JOHN MUST BUY HOUSE
   50: *POSS *SEE BUY CAR *IX                                        FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *FUTURE BUY HOUSE                                 JOHN SHOULD NOT BUY HOUSE
   57: *MARY *JOHN *IX MARY                                          JOHN DECIDE VISIT MARY
   67: *TELL FUTURE *WHO BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE *GO MARY                                         JOHN WILL VISIT MARY
   74: *IX *MARY *MARY MARY                                          JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *IX *ARRIVE *HOMEWORK BOOK                                    IX-1P FIND SOMETHING-ONE BOOK
   89: JOHN IX *IX *IX IX NEW COAT                                   JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *SOMETHING-ONE IX *IX *MARY BOOK                         JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *IX *WOMAN *WOMAN WOMAN BOOK                             JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: *FRANK *POSS                                                  JOHN LEG
  107: JOHN *JOHN *HAVE *GO *JOHN                                    JOHN POSS FRIEND HAVE CANDY
  108: *IX *BOOK                                                     WOMAN ARRIVE
  113: *JOHN CAR *CAR *JOHN *BOX                                     IX CAR BLUE SUE BUY
  119: *MARY *BUY1 *CAR CAR *HAVE                                    SUE BUY IX CAR BLUE
  122: JOHN *HOUSE BOOK                                              JOHN READ BOOK
  139: JOHN *BUY1 *BOX YESTERDAY BOOK                                JOHN BUY WHAT YESTERDAY BOOK
  142: *FRANK *NEW YESTERDAY WHAT BOOK                               JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *MARY WHO                                                LOVE JOHN WHO
  167: *MARY *SOMETHING-ONE *MARY *MARY *LOVE                        JOHN IX SAY LOVE MARY
  171: *MARY *JOHN BLAME                                             JOHN MARY BLAME
  174: *CAR *GIVE3 GIVE1 *MARY *BLAME                                PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER APPLE                                  ALL BOY GIVE TEACHER APPLE
  189: *JANA *SOMETHING-ONE *YESTERDAY BOX                           JOHN GIVE GIRL BOX
  193: JOHN *SOMETHING-ONE *YESTERDAY BOX                            JOHN GIVE GIRL BOX
  199: *JOHN CHOCOLATE WHO                                           LIKE CHOCOLATE WHO
  201: JOHN *MAN *WOMAN *LOVE BUY HOUSE                              JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:04:25 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:04:25 PM' - root - DEBUG - Please wait...
'19/04/2017 04:05:09 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:05:09 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta, right
Chosen Model Selector:  SelectorCV
Training complete for JOHN with 4 states with time 31.449308013019618 seconds
Training complete for WRITE with 10 states with time 0.24526109301950783 seconds
Training complete for HOMEWORK with 7 states with time 0.22202192002441734 seconds
Training complete for IX-1P with 2 states with time 0.5931486150366254 seconds
Training complete for SEE with 3 states with time 0.8945022549596615 seconds
Training complete for YESTERDAY with 2 states with time 1.3355764099978842 seconds
Training complete for IX with 3 states with time 9.326122457976453 seconds
Training complete for LOVE with 3 states with time 1.9508756109862588 seconds
Training complete for MARY with 10 states with time 8.265192974999081 seconds
Training complete for CAN with 2 states with time 2.242794410965871 seconds
Training complete for GO with 4 states with time 1.2773863929905929 seconds
Training complete for GO1 with 5 states with time 0.6873136610374786 seconds
Training complete for FUTURE with 2 states with time 2.0596084679709747 seconds
Training complete for GO2 with 4 states with time 0.09205947100417688 seconds
Training complete for PARTY with 7 states with time 0.17394700401928276 seconds
Training complete for FUTURE1 with 5 states with time 0.19492436200380325 seconds
Training complete for HIT with 7 states with time 0.1649277780088596 seconds
Training complete for BLAME with 3 states with time 0.8333018979756162 seconds
Training complete for FRED with 4 states with time 0.2165071819908917 seconds
Training complete for FISH with 5 states with time 0.26260265801101923 seconds
Training complete for WONT with 2 states with time 0.4551541510154493 seconds
Training complete for EAT with 2 states with time 0.38036557601299137 seconds
Training complete for BUT with 8 states with time 0.22898435994284227 seconds
Training complete for CHICKEN with 7 states with time 0.3040554419858381 seconds
Training complete for VEGETABLE with 2 states with time 1.112540572998114 seconds
Training complete for CHINA with 10 states with time 0.21840244700433686 seconds
Training complete for PEOPLE with 2 states with time 0.7438695399905555 seconds
Training complete for PREFER with 2 states with time 0.6502769169746898 seconds
Training complete for BROCCOLI with 8 states with time 0.3392314509837888 seconds
Training complete for LIKE with 2 states with time 1.4442965380148962 seconds
Training complete for LEAVE with 5 states with time 0.4091637469828129 seconds
Training complete for SAY with 5 states with time 0.2379216940025799 seconds
Training complete for BUY with 5 states with time 2.3276494479505345 seconds
Training complete for HOUSE with 2 states with time 1.6313682930194773 seconds
Training complete for KNOW with 2 states with time 0.3166233639931306 seconds
Training complete for CORN with 2 states with time 0.5605908950092271 seconds
Training complete for CORN1 with 8 states with time 0.244647808955051 seconds
Training complete for THINK with 4 states with time 0.21401008497923613 seconds
Training complete for NOT with 2 states with time 1.1144478549831547 seconds
Training complete for PAST with 4 states with time 0.1988711070152931 seconds
Training complete for LIVE with 3 states with time 0.08167679701000452 seconds
Training complete for CHICAGO with 8 states with time 0.18205745302839205 seconds
Training complete for CAR with 2 states with time 2.0543946069665253 seconds
Training complete for SHOULD with 4 states with time 1.3326184659963474 seconds
Training complete for DECIDE with 7 states with time 0.2206005859770812 seconds
Training complete for VISIT with 2 states with time 1.3778650860185735 seconds
Training complete for MOVIE with 7 states with time 0.22260242502670735 seconds
Training complete for WANT with 8 states with time 0.21566214400809258 seconds
Training complete for SELL with 4 states with time 0.6053453020285815 seconds
Training complete for TOMORROW with 9 states with time 0.18438796798000112 seconds
Training complete for NEXT-WEEK with 5 states with time 0.09968108602333814 seconds
Training complete for NEW-YORK with 7 states with time 0.2278369539999403 seconds
Training complete for LAST-WEEK with 9 states with time 0.20207592897349969 seconds
Training complete for WILL with 5 states with time 0.22166146896779537 seconds
Training complete for FINISH with 2 states with time 0.747616115026176 seconds
Training complete for ANN with 4 states with time 0.19013511802768335 seconds
Training complete for READ with 2 states with time 0.6272953640436754 seconds
Training complete for BOOK with 2 states with time 2.212125153047964 seconds
Training complete for CHOCOLATE with 2 states with time 0.5779025590163656 seconds
Training complete for FIND with 2 states with time 0.04380204400513321 seconds
Training complete for SOMETHING-ONE with 2 states with time 1.4218404850107618 seconds
Training complete for POSS with 2 states with time 1.4834657110041007 seconds
Training complete for BROTHER with 10 states with time 0.2218147880048491 seconds
Training complete for ARRIVE with 2 states with time 1.9405272589647211 seconds
Training complete for HERE with 3 states with time 0.3050428970018402 seconds
Training complete for GIVE with 2 states with time 1.4939743329887278 seconds
Training complete for MAN with 10 states with time 0.2936911039869301 seconds
Training complete for NEW with 4 states with time 0.8347135849762708 seconds
Training complete for COAT with 10 states with time 0.2616294120089151 seconds
Training complete for WOMAN with 2 states with time 1.2376141110435128 seconds
Training complete for GIVE1 with 2 states with time 1.220975834003184 seconds
Training complete for HAVE with 2 states with time 0.7390658439835533 seconds
Training complete for FRANK with 2 states with time 0.5443010979797691 seconds
Training complete for BREAK-DOWN with 2 states with time 0.6278540139901452 seconds
Training complete for SEARCH-FOR with 8 states with time 0.1902836459921673 seconds
Training complete for WHO with 4 states with time 2.222843785013538 seconds
Training complete for WHAT with 10 states with time 3.0292373480042443 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 0.19771756697446108 seconds
Training complete for CANDY with 2 states with time 0.19418247399153188 seconds
Training complete for BLUE with 2 states with time 0.28552789700916037 seconds
Training complete for SUE with 2 states with time 0.5996502240304835 seconds
Training complete for BUY1 with 6 states with time 0.8465528080123477 seconds
Training complete for STOLEN with 8 states with time 0.24853046203497797 seconds
Training complete for OLD with 2 states with time 0.1549931179615669 seconds
Training complete for STUDENT with 2 states with time 0.4012035910272971 seconds
Training complete for VIDEOTAPE with 2 states with time 0.3987283220048994 seconds
Training complete for BORROW with 3 states with time 0.08927892398787662 seconds
Training complete for MOTHER with 2 states with time 0.4000054099597037 seconds
Training complete for POTATO with 5 states with time 0.24963035102700815 seconds
Training complete for TELL with 2 states with time 0.9289098889566958 seconds
Training complete for BILL with 2 states with time 0.9173858739668503 seconds
Training complete for THROW with 4 states with time 0.7530470780329779 seconds
Training complete for APPLE with 2 states with time 0.7533346600248478 seconds
Training complete for NAME with 10 states with time 0.19998966000275686 seconds
Training complete for SHOOT with 10 states with time 0.2066911730216816 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 0.22347310197073966 seconds
Training complete for GROUP with 5 states with time 0.1519798919907771 seconds
Training complete for JANA with 10 states with time 0.22969582601217553 seconds
Training complete for TOY1 with 9 states with time 0.19324262399459258 seconds
Training complete for MANY with 4 states with time 0.15038182499120012 seconds
Training complete for TOY with 4 states with time 0.20756325701950118 seconds
Training complete for ALL with 9 states with time 0.21712566597852856 seconds
Training complete for BOY with 4 states with time 0.37418751197401434 seconds
Training complete for TEACHER with 4 states with time 0.6547346169827506 seconds
Training complete for GIRL with 2 states with time 0.4056590379914269 seconds
Training complete for BOX with 2 states with time 1.2659736759960651 seconds
Training complete for GIVE2 with 9 states with time 0.2480513799819164 seconds
Training complete for GIVE3 with 10 states with time 0.2966529600089416 seconds
Training complete for GET with 7 states with time 0.12831686699064448 seconds
Training complete for PUTASIDE with 4 states with time 0.20202665601391345 seconds
Number of word models returned = 112
'19/04/2017 04:07:20 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:07:20 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:07:31 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5617977528089888
Total correct: 78 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *BOOK *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN *HAVE GO *HAVE                                           JOHN CAN GO CAN
   12: JOHN CAN *CAN CAN                                             JOHN CAN GO CAN
   21: JOHN *NEW *JOHN *MARY *CAR *CAR *VISIT *VISIT                 JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: *MARY *MARY IX *MARY IX                                       JOHN LIKE IX IX IX
   28: JOHN *MARY IX *LIKE IX                                        JOHN LIKE IX IX IX
   30: *IX LIKE *MARY *LIKE IX                                       JOHN LIKE IX IX IX
   36: MARY *PREFER *GIRL *GIVE *MARY *JOHN                          MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *CORN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: JOHN *POSS BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *FRANK *SEE BUY CAR SHOULD                                    FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *MARY BUY HOUSE                                   JOHN SHOULD NOT BUY HOUSE
   57: *IX *SUE VISIT *IX                                            JOHN DECIDE VISIT MARY
   67: JOHN *POSS NOT BUY HOUSE                                      JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FINISH *GO MARY                                         JOHN WILL VISIT MARY
   74: *IX *MARY VISIT *GO                                           JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *LOVE *ARRIVE *POSS BOOK                                      IX-1P FIND SOMETHING-ONE BOOK
   89: JOHN *SOMETHING-ONE *IX *IX *SOMETHING-ONE NEW *BREAK-DOWN    JOHN IX GIVE MAN IX NEW COAT
   90: *MARY *SOMETHING-ONE *SOMETHING-ONE SOMETHING-ONE WOMAN BOOK  JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *GIVE1 *WOMAN *WOMAN WOMAN BOOK                          JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: *FRANK NEW CAR BREAK-DOWN                                     POSS NEW CAR BREAK-DOWN
  105: *FRANK *POSS                                                  JOHN LEG
  107: JOHN *SOMETHING-ONE *HAVE *GO *MARY                           JOHN POSS FRIEND HAVE CANDY
  108: *IX *BOOK                                                     WOMAN ARRIVE
  113: *SOMETHING-ONE CAR *GO *JOHN *BOX                             IX CAR BLUE SUE BUY
  119: *PREFER *BUY1 *GO *HAVE *GO                                   SUE BUY IX CAR BLUE
  122: JOHN *HOUSE BOOK                                              JOHN READ BOOK
  139: JOHN *BUY1 WHAT YESTERDAY BOOK                                JOHN BUY WHAT YESTERDAY BOOK
  142: *FRANK BUY YESTERDAY WHAT BOOK                                JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *VISIT WHO                                               LOVE JOHN WHO
  167: *MARY *SOMETHING-ONE *VISIT LOVE *LOVE                        JOHN IX SAY LOVE MARY
  171: *MARY *JOHN BLAME                                             JOHN MARY BLAME
  174: *GIVE1 *GIVE1 GIVE1 *APPLE *VISIT                             PEOPLE GROUP GIVE1 JANA TOY
  181: *SUE *BOX                                                     JOHN ARRIVE
  184: *GIVE BOY *GIVE1 TEACHER APPLE                                ALL BOY GIVE TEACHER APPLE
  189: JOHN *SOMETHING-ONE *YESTERDAY BOX                            JOHN GIVE GIRL BOX
  193: JOHN *GIVE1 *YESTERDAY BOX                                    JOHN GIVE GIRL BOX
  199: *LOVE CHOCOLATE *MARY                                         LIKE CHOCOLATE WHO
  201: JOHN *MARY *WOMAN *LOVE BUY HOUSE                             JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:07:31 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:07:31 PM' - root - DEBUG - Please wait...
'19/04/2017 04:08:16 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:08:16 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta, right
Chosen Model Selector:  SelectorBIC
Training complete for JOHN with 10 states with time 21.11578322702553 seconds
Training complete for WRITE with 10 states with time 0.24450534500647336 seconds
Training complete for HOMEWORK with 7 states with time 0.23223987402161583 seconds
Training complete for IX-1P with 9 states with time 0.32709235296351835 seconds
Training complete for SEE with 10 states with time 0.530460280016996 seconds
Training complete for YESTERDAY with 10 states with time 0.550129217968788 seconds
Training complete for IX with 10 states with time 4.831824263033923 seconds
Training complete for LOVE with 10 states with time 1.066847364010755 seconds
Training complete for MARY with 10 states with time 4.032522427034564 seconds
Training complete for CAN with 10 states with time 1.2804405359784141 seconds
Training complete for GO with 10 states with time 0.7022017519921064 seconds
Training complete for GO1 with 10 states with time 0.32465998898260295 seconds
Training complete for FUTURE with 10 states with time 0.9566978940274566 seconds
Training complete for GO2 with 4 states with time 0.08490119897760451 seconds
Training complete for PARTY with 7 states with time 0.16180647601140663 seconds
Training complete for FUTURE1 with 5 states with time 0.1915351619827561 seconds
Training complete for HIT with 7 states with time 0.16080777801107615 seconds
Training complete for BLAME with 10 states with time 0.32190184597857296 seconds
Training complete for FRED with 4 states with time 0.15823214501142502 seconds
Training complete for FISH with 5 states with time 0.2117660519434139 seconds
Training complete for WONT with 8 states with time 0.24298280698712915 seconds
Training complete for EAT with 6 states with time 0.28617105702869594 seconds
Training complete for BUT with 8 states with time 0.22045150998746976 seconds
Training complete for CHICKEN with 7 states with time 0.2194691959884949 seconds
Training complete for VEGETABLE with 10 states with time 0.4125095990020782 seconds
Training complete for CHINA with 10 states with time 0.20769480196759105 seconds
Training complete for PEOPLE with 10 states with time 0.280552951968275 seconds
Training complete for PREFER with 10 states with time 0.354628274042625 seconds
Training complete for BROCCOLI with 8 states with time 0.2573669039993547 seconds
Training complete for LIKE with 9 states with time 0.6003159250249155 seconds
Training complete for LEAVE with 10 states with time 0.23757166595896706 seconds
Training complete for SAY with 5 states with time 0.1999381849891506 seconds
Training complete for BUY with 10 states with time 1.2651548539870419 seconds
Training complete for HOUSE with 10 states with time 0.6702216639532708 seconds
Training complete for KNOW with 3 states with time 0.22165747999679297 seconds
Training complete for CORN with 6 states with time 0.3257717819651589 seconds
Training complete for CORN1 with 6 states with time 0.2513318069977686 seconds
Training complete for THINK with 4 states with time 0.21674484299728647 seconds
Training complete for NOT with 10 states with time 0.5613057779846713 seconds
Training complete for PAST with 4 states with time 0.20676482998533174 seconds
Training complete for LIVE with 3 states with time 0.09046960901468992 seconds
Training complete for CHICAGO with 8 states with time 0.20492356998147443 seconds
Training complete for CAR with 9 states with time 1.399737271014601 seconds
Training complete for SHOULD with 10 states with time 0.6651381450355984 seconds
Training complete for DECIDE with 7 states with time 0.2672060769982636 seconds
Training complete for VISIT with 10 states with time 0.7371748560108244 seconds
Training complete for MOVIE with 7 states with time 0.27379771100822836 seconds
Training complete for WANT with 8 states with time 0.25468054600059986 seconds
Training complete for SELL with 10 states with time 0.29021235200343654 seconds
Training complete for TOMORROW with 9 states with time 0.2195781070040539 seconds
Training complete for NEXT-WEEK with 5 states with time 0.14288805599790066 seconds
Training complete for NEW-YORK with 7 states with time 0.2413169299834408 seconds
Training complete for LAST-WEEK with 9 states with time 0.19754181703319773 seconds
Training complete for WILL with 5 states with time 0.21048693702323362 seconds
Training complete for FINISH with 10 states with time 0.3606710649910383 seconds
Training complete for ANN with 4 states with time 0.260313926031813 seconds
Training complete for READ with 10 states with time 0.3006683600251563 seconds
Training complete for BOOK with 10 states with time 1.1877315019955859 seconds
Training complete for CHOCOLATE with 10 states with time 0.37075802200706676 seconds
Training complete for FIND with 2 states with time 0.05265115003567189 seconds
Training complete for SOMETHING-ONE with 10 states with time 0.7439052300178446 seconds
Training complete for POSS with 8 states with time 0.750003983033821 seconds
Training complete for BROTHER with 10 states with time 0.24771664495347068 seconds
Training complete for ARRIVE with 10 states with time 1.2997107510454953 seconds
Training complete for HERE with 10 states with time 0.2627191439969465 seconds
Training complete for GIVE with 10 states with time 0.8403910369961523 seconds
Training complete for MAN with 10 states with time 0.3999880239716731 seconds
Training complete for NEW with 10 states with time 0.3940426320186816 seconds
Training complete for COAT with 10 states with time 0.31621661596000195 seconds
Training complete for WOMAN with 10 states with time 0.799592480994761 seconds
Training complete for GIVE1 with 10 states with time 0.7827734960010275 seconds
Training complete for HAVE with 10 states with time 0.3514295549830422 seconds
Training complete for FRANK with 10 states with time 0.35867472703102976 seconds
Training complete for BREAK-DOWN with 8 states with time 0.3679602849879302 seconds
Training complete for SEARCH-FOR with 7 states with time 0.20135978795588017 seconds
Training complete for WHO with 10 states with time 2.0128945839824155 seconds
Training complete for WHAT with 10 states with time 2.0221555259777233 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 0.1847818369860761 seconds
Training complete for CANDY with 2 states with time 0.19306629401398823 seconds
Training complete for BLUE with 6 states with time 0.31775004899827763 seconds
Training complete for SUE with 10 states with time 0.37405369197949767 seconds
Training complete for BUY1 with 10 states with time 0.3943365630111657 seconds
Training complete for STOLEN with 8 states with time 0.2431346070370637 seconds
Training complete for OLD with 2 states with time 0.17191317497054115 seconds
Training complete for STUDENT with 10 states with time 0.29774568596621975 seconds
Training complete for VIDEOTAPE with 9 states with time 0.2860311639960855 seconds
Training complete for BORROW with 3 states with time 0.08104896097211167 seconds
Training complete for MOTHER with 9 states with time 0.2420189330005087 seconds
Training complete for POTATO with 5 states with time 0.17367836402263492 seconds
Training complete for TELL with 10 states with time 0.30791251797927544 seconds
Training complete for BILL with 10 states with time 0.4299246260197833 seconds
Training complete for THROW with 10 states with time 0.2645557500072755 seconds
Training complete for APPLE with 10 states with time 0.34189874603180215 seconds
Training complete for NAME with 7 states with time 0.1880499140243046 seconds
Training complete for SHOOT with 10 states with time 0.19330603099660948 seconds
Training failed for SAY-1P
Training complete for SELF with 9 states with time 0.22083978803129867 seconds
Training complete for GROUP with 5 states with time 0.1604399560019374 seconds
Training complete for JANA with 10 states with time 0.25842914602253586 seconds
Training complete for TOY1 with 8 states with time 0.22534818499116227 seconds
Training complete for MANY with 4 states with time 0.1593846469768323 seconds
Training complete for TOY with 4 states with time 0.20451444300124422 seconds
Training complete for ALL with 9 states with time 0.24368245602818206 seconds
Training complete for BOY with 10 states with time 0.27915580198168755 seconds
Training complete for TEACHER with 10 states with time 0.3908865709672682 seconds
Training complete for GIRL with 10 states with time 0.4003403400420211 seconds
Training complete for BOX with 10 states with time 0.46244145097443834 seconds
Training complete for GIVE2 with 9 states with time 0.19903520098887384 seconds
Training complete for GIVE3 with 10 states with time 0.2538243369781412 seconds
Training complete for GET with 7 states with time 0.1254462000215426 seconds
Training complete for PUTASIDE with 4 states with time 0.23212324600899592 seconds
Number of word models returned = 112
'19/04/2017 04:09:41 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:09:41 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:09:52 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.48314606741573035
Total correct: 92 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *NEW *ARRIVE                                             JOHN WRITE HOMEWORK
    7: JOHN *VISIT GO CAN                                            JOHN CAN GO CAN
   12: JOHN CAN *JOHN CAN                                            JOHN CAN GO CAN
   21: JOHN *JOHN *JOHN *JOHN *CAR *CAR *FUTURE *FUTURE              JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *MARY *LOVE IX IX                                        JOHN LIKE IX IX IX
   28: JOHN *MARY IX *MARY IX                                        JOHN LIKE IX IX IX
   30: *IX *IX *MARY IX IX                                           JOHN LIKE IX IX IX
   36: MARY *JOHN *IX IX *MARY *MARY                                 MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *CORN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: JOHN *JOHN BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *JOHN *SEE BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *MARY BUY HOUSE                                   JOHN SHOULD NOT BUY HOUSE
   57: *IX *JOHN *GO *IX                                             JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *JOHN BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *MARY VISIT MARY                                          JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *ARRIVE *CAR BOOK                                       IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *POSS *WOMAN *WOMAN IX *ARRIVE *BREAK-DOWN              JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX WOMAN BOOK                                    JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *WOMAN IX *IX WOMAN BOOK                                 JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *FRANK                                                   JOHN LEG
  107: JOHN *IX *JOHN *IX *IX                                        JOHN POSS FRIEND HAVE CANDY
  108: *JOHN ARRIVE                                                  WOMAN ARRIVE
  113: IX CAR *IX *MARY *BOX                                         IX CAR BLUE SUE BUY
  119: *MARY *BUY1 IX CAR *MARY                                      SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: *IX *BUY1 WHAT *JOHN BOOK                                     JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *VISIT LOVE MARY                                      JOHN IX SAY LOVE MARY
  171: JOHN MARY BLAME                                               JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *IX *WHAT                                  PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER *GO                                    ALL BOY GIVE TEACHER APPLE
  189: JOHN *IX *VISIT BOX                                           JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *FUTURE *WOMAN *JOHN BUY HOUSE                           JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:09:52 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:09:52 PM' - root - DEBUG - Please wait...
'19/04/2017 04:10:34 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:10:34 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta, right
Chosen Model Selector:  SelectorDIC
Training complete for JOHN with 10 states with time 22.82980879198294 seconds
Training complete for WRITE with 9 states with time 2.0637699179933406 seconds
Training complete for HOMEWORK with 5 states with time 0.7929504909552634 seconds
Training complete for IX-1P with 9 states with time 2.054524907958694 seconds
Training complete for SEE with 10 states with time 2.4741074849735014 seconds
Training complete for YESTERDAY with 10 states with time 2.305727905011736 seconds
Training complete for IX with 10 states with time 6.52479683799902 seconds
Training complete for LOVE with 10 states with time 2.7746846709633246 seconds
Training complete for MARY with 10 states with time 5.522092082013842 seconds
Training complete for CAN with 9 states with time 2.964610044960864 seconds
Training complete for GO with 10 states with time 2.387229538988322 seconds
Training complete for GO1 with 10 states with time 2.108737927977927 seconds
Training complete for FUTURE with 9 states with time 2.609917563968338 seconds
Training complete for GO2 with 4 states with time 0.61349043098744 seconds
Training complete for PARTY with 7 states with time 1.3241082069580443 seconds
Training complete for FUTURE1 with 5 states with time 0.8338471619645134 seconds
Training complete for HIT with 7 states with time 1.3083337650168687 seconds
Training complete for BLAME with 10 states with time 2.0776175790233538 seconds
Training complete for FRED with 4 states with time 0.5880097079789266 seconds
Training complete for FISH with 3 states with time 0.8015227199648507 seconds
Training complete for WONT with 8 states with time 1.5307135800248943 seconds
Training complete for EAT with 6 states with time 1.0564310940098949 seconds
Training complete for BUT with 8 states with time 1.6431691130273975 seconds
Training complete for CHICKEN with 7 states with time 1.344438329047989 seconds
Training complete for VEGETABLE with 2 states with time 2.2867391839972697 seconds
Training complete for CHINA with 9 states with time 2.27814650000073 seconds
Training complete for PEOPLE with 10 states with time 2.076708165986929 seconds
Training complete for PREFER with 10 states with time 2.261900447017979 seconds
Training complete for BROCCOLI with 8 states with time 1.69141262100311 seconds
Training complete for LIKE with 9 states with time 2.7311305649927817 seconds
Training complete for LEAVE with 4 states with time 2.4648817199631594 seconds
Training complete for SAY with 2 states with time 0.8290835480438545 seconds
Training complete for BUY with 10 states with time 3.182684840983711 seconds
Training complete for HOUSE with 10 states with time 2.571793456969317 seconds
Training complete for KNOW with 2 states with time 0.48694784595863894 seconds
Training complete for CORN with 2 states with time 1.5921272730338387 seconds
Training complete for CORN1 with 2 states with time 1.1651060289586894 seconds
Training complete for THINK with 3 states with time 0.7310166289680637 seconds
Training complete for NOT with 9 states with time 2.7319508049986325 seconds
Training complete for PAST with 2 states with time 0.6622463800013065 seconds
Training complete for LIVE with 3 states with time 0.4495288690086454 seconds
Training complete for CHICAGO with 8 states with time 1.787433265009895 seconds
Training complete for CAR with 10 states with time 3.3420932040316984 seconds
Training complete for SHOULD with 10 states with time 2.774767428985797 seconds
Training complete for DECIDE with 7 states with time 1.4917018699925393 seconds
Training complete for VISIT with 10 states with time 2.4222367109614424 seconds
Training complete for MOVIE with 7 states with time 1.4107385499519296 seconds
Training complete for WANT with 8 states with time 1.8100706749828532 seconds
Training complete for SELL with 10 states with time 2.174828218994662 seconds
Training complete for TOMORROW with 9 states with time 1.9353843710268848 seconds
Training complete for NEXT-WEEK with 5 states with time 0.8546533100306988 seconds
Training complete for NEW-YORK with 7 states with time 1.3456199149950407 seconds
Training complete for LAST-WEEK with 9 states with time 1.816873331030365 seconds
Training complete for WILL with 5 states with time 0.8011853729840368 seconds
Training complete for FINISH with 9 states with time 2.1956570009933785 seconds
Training complete for ANN with 2 states with time 0.6627144139492884 seconds
Training complete for READ with 10 states with time 2.1776836860226467 seconds
Training complete for BOOK with 10 states with time 2.8550078280386515 seconds
Training complete for CHOCOLATE with 9 states with time 2.123317076009698 seconds
Training complete for FIND with 2 states with time 0.19552263797959313 seconds
Training complete for SOMETHING-ONE with 10 states with time 2.4944702869979665 seconds
Training complete for POSS with 8 states with time 2.50077553401934 seconds
Training complete for BROTHER with 8 states with time 2.088686061964836 seconds
Training complete for ARRIVE with 10 states with time 2.943978792987764 seconds
Training complete for HERE with 8 states with time 2.1588105550035834 seconds
Training complete for GIVE with 7 states with time 2.7040310369920917 seconds
Training complete for MAN with 3 states with time 2.673462398990523 seconds
Training complete for NEW with 10 states with time 2.1895647040219046 seconds
Training complete for COAT with 10 states with time 2.092109485005494 seconds
Training complete for WOMAN with 10 states with time 2.687855949974619 seconds
Training complete for GIVE1 with 10 states with time 2.5627327980473638 seconds
Training complete for HAVE with 9 states with time 2.451727135980036 seconds
Training complete for FRANK with 7 states with time 2.517083427985199 seconds
Training complete for BREAK-DOWN with 8 states with time 1.6598686380311847 seconds
Training complete for SEARCH-FOR with 7 states with time 1.6423636420513503 seconds
Training complete for WHO with 9 states with time 3.7071287189610302 seconds
Training complete for WHAT with 8 states with time 3.8206196220126003 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 1.084501873003319 seconds
Training complete for CANDY with 2 states with time 0.2122549309860915 seconds
Training complete for BLUE with 6 states with time 1.228548000974115 seconds
Training complete for SUE with 10 states with time 2.387753569986671 seconds
Training complete for BUY1 with 10 states with time 2.1737818230176345 seconds
Training complete for STOLEN with 8 states with time 1.614790044957772 seconds
Training complete for OLD with 2 states with time 0.19498505402589217 seconds
Training complete for STUDENT with 10 states with time 2.094139445980545 seconds
Training complete for VIDEOTAPE with 6 states with time 1.1521520029637031 seconds
Training complete for BORROW with 3 states with time 0.428414266963955 seconds
Training complete for MOTHER with 9 states with time 2.219108331017196 seconds
Training complete for POTATO with 5 states with time 0.9094157349900343 seconds
Training complete for TELL with 2 states with time 2.461786800005939 seconds
Training complete for BILL with 2 states with time 2.335955285001546 seconds
Training complete for THROW with 10 states with time 2.225977974012494 seconds
Training complete for APPLE with 8 states with time 2.6178692629910074 seconds
Training complete for NAME with 6 states with time 2.3408146490110084 seconds
Training complete for SHOOT with 10 states with time 2.365446701995097 seconds
Training failed for SAY-1P
Training complete for SELF with 8 states with time 2.193919974961318 seconds
Training complete for GROUP with 5 states with time 0.8718155029928312 seconds
Training complete for JANA with 7 states with time 2.3515718349954113 seconds
Training complete for TOY1 with 8 states with time 1.9081481519970112 seconds
Training complete for MANY with 4 states with time 0.8112424500286579 seconds
Training complete for TOY with 4 states with time 0.60703235398978 seconds
Training complete for ALL with 9 states with time 1.9818677640287206 seconds
Training complete for BOY with 10 states with time 2.4606252330122516 seconds
Training complete for TEACHER with 8 states with time 2.277025106945075 seconds
Training complete for GIRL with 5 states with time 1.4983201019931585 seconds
Training complete for BOX with 10 states with time 2.2180459499941207 seconds
Training complete for GIVE2 with 2 states with time 1.8714090889552608 seconds
Training complete for GIVE3 with 10 states with time 2.14198185200803 seconds
Training complete for GET with 7 states with time 1.5434072270290926 seconds
Training complete for PUTASIDE with 4 states with time 0.6348649930441752 seconds
Number of word models returned = 112
'19/04/2017 04:14:39 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:14:39 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:14:50 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.4943820224719101
Total correct: 90 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN WRITE *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN *VISIT GO CAN                                            JOHN CAN GO CAN
   12: JOHN *WHAT *WHAT CAN                                          JOHN CAN GO CAN
   21: JOHN *JOHN *JOHN *JOHN *CAR *CAR *CAN *FUTURE                 JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *MARY *LOVE IX IX                                        JOHN LIKE IX IX IX
   28: JOHN *MARY IX *MARY IX                                        JOHN LIKE IX IX IX
   30: *IX *IX *MARY IX IX                                           JOHN LIKE IX IX IX
   36: MARY *JOHN *GIRL IX *MARY *MARY                               MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *CORN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: JOHN *FUTURE BUY HOUSE                                        JOHN MUST BUY HOUSE
   50: *JOHN *SEE BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *FUTURE BUY HOUSE                                 JOHN SHOULD NOT BUY HOUSE
   57: *IX *JOHN *GO *IX                                             JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *JOHN BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *MARY VISIT MARY                                          JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *ARRIVE *JOHN BOOK                                      IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *POSS *WOMAN *WOMAN IX *ARRIVE *BREAK-DOWN              JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX WOMAN *VIDEOTAPE                              JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *WOMAN IX *IX WOMAN BOOK                                 JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *FRANK                                                   JOHN LEG
  107: JOHN *IX *JOHN *IX *IX                                        JOHN POSS FRIEND HAVE CANDY
  108: *JOHN ARRIVE                                                  WOMAN ARRIVE
  113: IX CAR *IX *MARY *BOX                                         IX CAR BLUE SUE BUY
  119: *MARY *BUY1 IX *JOHN *MARY                                    SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: *IX *BUY1 WHAT *WHAT BOOK                                     JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *VISIT LOVE MARY                                      JOHN IX SAY LOVE MARY
  171: JOHN MARY BLAME                                               JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *IX *BLAME                                 PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER *GO                                    ALL BOY GIVE TEACHER APPLE
  189: JOHN *IX *VISIT BOX                                           JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *FUTURE *WOMAN *JOHN BUY HOUSE                           JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:14:50 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:14:50 PM' - root - DEBUG - Please wait...
'19/04/2017 04:15:15 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:15:15 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, delta, right
Chosen Model Selector:  SelectorConstant
Training complete for JOHN with 3 states with time 1.1316968780010939 seconds
Training complete for WRITE with 3 states with time 0.017557198996655643 seconds
Training complete for HOMEWORK with 3 states with time 0.021339957020245492 seconds
Training complete for IX-1P with 3 states with time 0.03059953497722745 seconds
Training complete for SEE with 3 states with time 0.032366090978030115 seconds
Training complete for YESTERDAY with 3 states with time 0.04960453702369705 seconds
Training complete for IX with 3 states with time 0.4518484639702365 seconds
Training complete for LOVE with 3 states with time 0.061097302997950464 seconds
Training complete for MARY with 3 states with time 0.27593531605089083 seconds
Training complete for CAN with 3 states with time 0.09779524599434808 seconds
Training complete for GO with 3 states with time 0.06690645799972117 seconds
Training complete for GO1 with 3 states with time 0.03290317300707102 seconds
Training complete for FUTURE with 3 states with time 0.08085226197727025 seconds
Training complete for GO2 with 3 states with time 0.017119608994107693 seconds
Training complete for PARTY with 3 states with time 0.014311078004539013 seconds
Training complete for FUTURE1 with 3 states with time 0.019370439986232668 seconds
Training complete for HIT with 3 states with time 0.015208040014840662 seconds
Training complete for BLAME with 3 states with time 0.025587427022401243 seconds
Training complete for FRED with 3 states with time 0.015316310978960246 seconds
Training complete for FISH with 3 states with time 0.02659039100399241 seconds
Training complete for WONT with 3 states with time 0.021127332001924515 seconds
Training complete for EAT with 3 states with time 0.024922130978666246 seconds
Training complete for BUT with 3 states with time 0.023755238973535597 seconds
Training complete for CHICKEN with 3 states with time 0.028589678986463696 seconds
Training complete for VEGETABLE with 3 states with time 0.03000192402396351 seconds
Training complete for CHINA with 3 states with time 0.022816730954218656 seconds
Training complete for PEOPLE with 3 states with time 0.03545148397097364 seconds
Training complete for PREFER with 3 states with time 0.029180338024161756 seconds
Training complete for BROCCOLI with 3 states with time 0.024372568994294852 seconds
Training complete for LIKE with 3 states with time 0.059722714009694755 seconds
Training complete for LEAVE with 3 states with time 0.022095947002526373 seconds
Training complete for SAY with 3 states with time 0.016760230995714664 seconds
Training complete for BUY with 3 states with time 0.07215294003253803 seconds
Training complete for HOUSE with 3 states with time 0.055789475969504565 seconds
Training complete for KNOW with 3 states with time 0.018860044016037136 seconds
Training complete for CORN with 3 states with time 0.02366375195560977 seconds
Training complete for CORN1 with 3 states with time 0.020164260000456125 seconds
Training complete for THINK with 3 states with time 0.01600634097121656 seconds
Training complete for NOT with 3 states with time 0.04729586699977517 seconds
Training complete for PAST with 3 states with time 0.021966409985907376 seconds
Training complete for LIVE with 3 states with time 0.018578177026938647 seconds
Training complete for CHICAGO with 3 states with time 0.01821112196194008 seconds
Training complete for CAR with 3 states with time 0.0836243350058794 seconds
Training complete for SHOULD with 3 states with time 0.056802080012857914 seconds
Training complete for DECIDE with 3 states with time 0.018116597027983516 seconds
Training complete for VISIT with 3 states with time 0.09708603605395183 seconds
Training complete for MOVIE with 3 states with time 0.016654170001856983 seconds
Training complete for WANT with 3 states with time 0.01792520802700892 seconds
Training complete for SELL with 3 states with time 0.018942785973194987 seconds
Training complete for TOMORROW with 3 states with time 0.016022234980482608 seconds
Training complete for NEXT-WEEK with 3 states with time 0.013293020019773394 seconds
Training complete for NEW-YORK with 3 states with time 0.017205320997163653 seconds
Training complete for LAST-WEEK with 3 states with time 0.018691106990445405 seconds
Training complete for WILL with 3 states with time 0.018998957995790988 seconds
Training complete for FINISH with 3 states with time 0.03515686100581661 seconds
Training complete for ANN with 3 states with time 0.018322322983294725 seconds
Training complete for READ with 3 states with time 0.023558148997835815 seconds
Training complete for BOOK with 3 states with time 0.0948599919793196 seconds
Training complete for CHOCOLATE with 3 states with time 0.03465581400087103 seconds
Training complete for FIND with 3 states with time 0.01366087602218613 seconds
Training complete for SOMETHING-ONE with 3 states with time 0.07779313903301954 seconds
Training complete for POSS with 3 states with time 0.05486003996338695 seconds
Training complete for BROTHER with 3 states with time 0.02111657097702846 seconds
Training complete for ARRIVE with 3 states with time 0.07184089097427204 seconds
Training complete for HERE with 3 states with time 0.019176238973159343 seconds
Training complete for GIVE with 3 states with time 0.06968044204404578 seconds
Training complete for MAN with 3 states with time 0.026864259038120508 seconds
Training complete for NEW with 3 states with time 0.0328193039749749 seconds
Training complete for COAT with 3 states with time 0.018803240032866597 seconds
Training complete for WOMAN with 3 states with time 0.03782104101264849 seconds
Training complete for GIVE1 with 3 states with time 0.047908529988490045 seconds
Training complete for HAVE with 3 states with time 0.02825006895000115 seconds
Training complete for FRANK with 3 states with time 0.02118920796783641 seconds
Training complete for BREAK-DOWN with 3 states with time 0.0245193510199897 seconds
Training complete for SEARCH-FOR with 3 states with time 0.014635675004683435 seconds
Training complete for WHO with 3 states with time 0.11530206800671294 seconds
Training complete for WHAT with 3 states with time 0.221524260006845 seconds
Training complete for LEG with 3 states with time 0.016136192018166184 seconds
Training complete for FRIEND with 3 states with time 0.018163760018069297 seconds
Training complete for CANDY with 3 states with time 0.0161619620048441 seconds
Training complete for BLUE with 3 states with time 0.02379571698838845 seconds
Training complete for SUE with 3 states with time 0.020040540024638176 seconds
Training complete for BUY1 with 3 states with time 0.04175399098312482 seconds
Training complete for STOLEN with 3 states with time 0.016412368044257164 seconds
Training complete for OLD with 3 states with time 0.015271169017069042 seconds
Training complete for STUDENT with 3 states with time 0.022892534034326673 seconds
Training complete for VIDEOTAPE with 3 states with time 0.020943715993780643 seconds
Training complete for BORROW with 3 states with time 0.015982942015398294 seconds
Training complete for MOTHER with 3 states with time 0.02064563799649477 seconds
Training complete for POTATO with 3 states with time 0.015293161966837943 seconds
Training complete for TELL with 3 states with time 0.0258226310252212 seconds
Training complete for BILL with 3 states with time 0.025811828032601625 seconds
Training complete for THROW with 3 states with time 0.0290744939702563 seconds
Training complete for APPLE with 3 states with time 0.035560850985348225 seconds
Training complete for NAME with 3 states with time 0.012864052026998252 seconds
Training complete for SHOOT with 3 states with time 0.015415504982229322 seconds
Training complete for SAY-1P with 3 states with time 0.014526751008816063 seconds
Training complete for SELF with 3 states with time 0.017427107959520072 seconds
Training complete for GROUP with 3 states with time 0.015982140030246228 seconds
Training complete for JANA with 3 states with time 0.029908043972682208 seconds
Training complete for TOY1 with 3 states with time 0.01672240800689906 seconds
Training complete for MANY with 3 states with time 0.01584461994934827 seconds
Training complete for TOY with 3 states with time 0.016324549971614033 seconds
Training complete for ALL with 3 states with time 0.02581516798818484 seconds
Training complete for BOY with 3 states with time 0.021971107984427363 seconds
Training complete for TEACHER with 3 states with time 0.037661600043065846 seconds
Training complete for GIRL with 3 states with time 0.03311360802035779 seconds
Training complete for BOX with 3 states with time 0.050733711977954954 seconds
Training complete for GIVE2 with 3 states with time 0.016448338981717825 seconds
Training complete for GIVE3 with 3 states with time 0.021896619990002364 seconds
Training complete for GET with 3 states with time 0.01482915598899126 seconds
Training complete for PUTASIDE with 3 states with time 0.014171126007568091 seconds
Number of word models returned = 112
'19/04/2017 04:15:27 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:15:27 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:15:36 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5898876404494382
Total correct: 73 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: *POSS WRITE HOMEWORK                                          JOHN WRITE HOMEWORK
    7: JOHN *HAVE GO *ARRIVE                                         JOHN CAN GO CAN
   12: *IX CAN *WHAT *HOUSE                                          JOHN CAN GO CAN
   21: *IX *HOMEWORK WONT *MARY *HOUSE *CAR *FUTURE *MARY            JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: *IX LIKE IX *LIKE IX                                          JOHN LIKE IX IX IX
   28: *IX *WHO *LIKE *LIKE IX                                       JOHN LIKE IX IX IX
   30: *LIKE LIKE *MARY *MARY IX                                     JOHN LIKE IX IX IX
   36: MARY *MARY *JOHN *GIVE *MARY *MARY                            MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN *GIVE *CORN MARY *MARY                                   JOHN IX THINK MARY LOVE
   43: *FRANK *POSS BUY HOUSE                                        JOHN MUST BUY HOUSE
   50: *POSS *POSS BUY CAR SHOULD                                    FUTURE JOHN BUY CAR SHOULD
   54: *IX SHOULD *MARY BUY HOUSE                                    JOHN SHOULD NOT BUY HOUSE
   57: JOHN *MARY *IX MARY                                           JOHN DECIDE VISIT MARY
   67: *LIKE *IX *MARY BUY HOUSE                                     JOHN FUTURE NOT BUY HOUSE
   71: *IX *SOMETHING-ONE VISIT MARY                                 JOHN WILL VISIT MARY
   74: *MARY *MARY *MARY MARY                                        JOHN NOT VISIT MARY
   77: *IX BLAME MARY                                                ANN BLAME MARY
   84: *IX *ARRIVE *HOMEWORK BOOK                                    IX-1P FIND SOMETHING-ONE BOOK
   89: *IX *SOMETHING-ONE *IX *IX IX NEW COAT                        JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *ALL *IX BOOK                                     JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: *IX *IX *WOMAN *WOMAN WOMAN BOOK                              JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: *IX *POSS                                                     JOHN LEG
  107: JOHN *IX *HAVE *GO *JOHN                                      JOHN POSS FRIEND HAVE CANDY
  108: *IX *BOOK                                                     WOMAN ARRIVE
  113: *JOHN CAR *IX *JOHN *IX                                       IX CAR BLUE SUE BUY
  119: *MARY *BUY1 IX CAR *IX                                        SUE BUY IX CAR BLUE
  122: JOHN *HOUSE *COAT                                             JOHN READ BOOK
  139: JOHN *BUY1 WHAT *WHAT BOOK                                    JOHN BUY WHAT YESTERDAY BOOK
  142: *IX *NEW YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *MARY WHO                                                LOVE JOHN WHO
  167: JOHN *SOMETHING-ONE *MARY *MARY *LOVE                         JOHN IX SAY LOVE MARY
  171: *MARY *IX BLAME                                               JOHN MARY BLAME
  174: *GIVE1 *GIVE3 GIVE1 *APPLE *BLAME                             PEOPLE GROUP GIVE1 JANA TOY
  181: *SOMETHING-ONE ARRIVE                                         JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER APPLE                                  ALL BOY GIVE TEACHER APPLE
  189: JOHN *JOHN *JOHN BOX                                          JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *IX CHOCOLATE WHO                                             LIKE CHOCOLATE WHO
  201: *IX *MAN *IX *LIKE BUY HOUSE                                  JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:15:36 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:15:36 PM' - root - DEBUG - Please wait...
'19/04/2017 04:16:01 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:16:01 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, delta, right
Chosen Model Selector:  SelectorCV
Training complete for JOHN with 2 states with time 34.56474725599401 seconds
Training complete for WRITE with 9 states with time 0.24787146202288568 seconds
Training complete for HOMEWORK with 8 states with time 0.22705524397315457 seconds
Training complete for IX-1P with 2 states with time 0.5964953160146251 seconds
Training complete for SEE with 5 states with time 1.0529299500049092 seconds
Training complete for YESTERDAY with 2 states with time 1.2813680249964818 seconds
Training complete for IX with 3 states with time 8.299076894996688 seconds
Training complete for LOVE with 2 states with time 2.1796397590078413 seconds
Training complete for MARY with 8 states with time 5.993529434024822 seconds
Training complete for CAN with 2 states with time 2.7612737719900906 seconds
Training complete for GO with 4 states with time 1.9553948829998262 seconds
Training complete for GO1 with 7 states with time 0.8552875080495141 seconds
Training complete for FUTURE with 2 states with time 2.6932924459688365 seconds
Training complete for GO2 with 5 states with time 0.16418553999392316 seconds
Training complete for PARTY with 7 states with time 0.1590809259796515 seconds
Training complete for FUTURE1 with 5 states with time 0.20350773696554825 seconds
Training complete for HIT with 7 states with time 0.16051902895560488 seconds
Training complete for BLAME with 2 states with time 0.9717203219770454 seconds
Training complete for FRED with 3 states with time 0.16956695599947125 seconds
Training complete for FISH with 4 states with time 0.22492904600221664 seconds
Training complete for WONT with 2 states with time 0.44827880000229925 seconds
Training complete for EAT with 2 states with time 0.3579714929801412 seconds
Training complete for BUT with 10 states with time 0.20733523601666093 seconds
Training complete for CHICKEN with 7 states with time 0.26620514201931655 seconds
Training complete for VEGETABLE with 2 states with time 1.0281413110205904 seconds
Training complete for CHINA with 10 states with time 0.23280275502474979 seconds
Training complete for PEOPLE with 2 states with time 0.7579377020010725 seconds
Training complete for PREFER with 2 states with time 0.636144909018185 seconds
Training complete for BROCCOLI with 7 states with time 0.26410640601534396 seconds
Training complete for LIKE with 2 states with time 1.1876288919593208 seconds
Training complete for LEAVE with 5 states with time 0.37360083899693564 seconds
Training complete for SAY with 3 states with time 0.20990479696774855 seconds
Training complete for BUY with 3 states with time 2.5418478610226884 seconds
Training complete for HOUSE with 2 states with time 2.0150900930166245 seconds
Training complete for KNOW with 2 states with time 0.3334747719927691 seconds
Training complete for CORN with 2 states with time 0.6868984420434572 seconds
Training complete for CORN1 with 3 states with time 0.28374032699503005 seconds
Training complete for THINK with 4 states with time 0.25622501102043316 seconds
Training complete for NOT with 2 states with time 1.2395795049960725 seconds
Training complete for PAST with 4 states with time 0.2003103059832938 seconds
Training complete for LIVE with 3 states with time 0.08640484296483919 seconds
Training complete for CHICAGO with 7 states with time 0.18403417099034414 seconds
Training complete for CAR with 4 states with time 2.482865222962573 seconds
Training complete for SHOULD with 4 states with time 1.8102323950151913 seconds
Training complete for DECIDE with 7 states with time 0.23653056303737685 seconds
Training complete for VISIT with 3 states with time 1.9666223999811336 seconds
Training complete for MOVIE with 7 states with time 0.2425488360458985 seconds
Training complete for WANT with 7 states with time 0.24632462504087016 seconds
Training complete for SELL with 4 states with time 0.6550847459584475 seconds
Training complete for TOMORROW with 10 states with time 0.18782680900767446 seconds
Training complete for NEXT-WEEK with 5 states with time 0.10777240502648056 seconds
Training complete for NEW-YORK with 8 states with time 0.25186376500641927 seconds
Training complete for LAST-WEEK with 10 states with time 0.1858913890318945 seconds
Training complete for WILL with 5 states with time 0.23733874299796298 seconds
Training complete for FINISH with 2 states with time 0.9437105260440148 seconds
Training failed for ANN
Training complete for READ with 2 states with time 0.662676508014556 seconds
Training complete for BOOK with 2 states with time 2.5948258269927464 seconds
Training complete for CHOCOLATE with 2 states with time 0.7994047359679826 seconds
Training complete for FIND with 2 states with time 0.046302876027766615 seconds
Training complete for SOMETHING-ONE with 3 states with time 1.6222494930261746 seconds
Training complete for POSS with 2 states with time 1.4392512259655632 seconds
Training complete for BROTHER with 10 states with time 0.24075474502751604 seconds
Training complete for ARRIVE with 2 states with time 2.347970750008244 seconds
Training complete for HERE with 3 states with time 0.4500491670332849 seconds
Training complete for GIVE with 4 states with time 2.0982968459720723 seconds
Training complete for MAN with 10 states with time 0.2803523589973338 seconds
Training complete for NEW with 2 states with time 1.1911264480440877 seconds
Training complete for COAT with 10 states with time 0.2794503640034236 seconds
Training complete for WOMAN with 2 states with time 1.1379199480288662 seconds
Training complete for GIVE1 with 2 states with time 1.475221547007095 seconds
Training complete for HAVE with 2 states with time 0.9169834610074759 seconds
Training complete for FRANK with 2 states with time 0.713195780001115 seconds
Training complete for BREAK-DOWN with 2 states with time 0.7226125390152447 seconds
Training complete for SEARCH-FOR with 10 states with time 0.19862488901708275 seconds
Training complete for WHO with 4 states with time 2.8316830540425144 seconds
Training complete for WHAT with 2 states with time 4.133148855995387 seconds
Training failed for LEG
Training complete for FRIEND with 8 states with time 0.21289849298773333 seconds
Training failed for CANDY
Training complete for BLUE with 2 states with time 0.3129121089586988 seconds
Training complete for SUE with 2 states with time 0.42777322698384523 seconds
Training complete for BUY1 with 4 states with time 0.9207435809657909 seconds
Training complete for STOLEN with 10 states with time 0.26896747504360974 seconds
Training complete for OLD with 2 states with time 0.16347371297888458 seconds
Training complete for STUDENT with 2 states with time 0.47669086896348745 seconds
Training complete for VIDEOTAPE with 2 states with time 0.482131564989686 seconds
Training complete for BORROW with 2 states with time 0.08264022599905729 seconds
Training complete for MOTHER with 2 states with time 0.5039243209757842 seconds
Training complete for POTATO with 5 states with time 0.1912944649811834 seconds
Training complete for TELL with 2 states with time 0.9386570339556783 seconds
Training complete for BILL with 4 states with time 1.1049770420067944 seconds
Training complete for THROW with 10 states with time 0.7501659750123508 seconds
Training complete for APPLE with 2 states with time 0.8155546860070899 seconds
Training complete for NAME with 10 states with time 0.24014043301576748 seconds
Training complete for SHOOT with 10 states with time 0.35489892098121345 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 0.23494118498638272 seconds
Training complete for GROUP with 4 states with time 0.15327196597354487 seconds
Training complete for JANA with 10 states with time 0.26480016903951764 seconds
Training complete for TOY1 with 9 states with time 0.27638802700676024 seconds
Training complete for MANY with 4 states with time 0.16230507101863623 seconds
Training complete for TOY with 4 states with time 0.21870701300213113 seconds
Training complete for ALL with 9 states with time 0.2668581429752521 seconds
Training complete for BOY with 2 states with time 0.4660436770063825 seconds
Training complete for TEACHER with 2 states with time 0.8521060229977593 seconds
Training complete for GIRL with 4 states with time 0.3953494270099327 seconds
Training complete for BOX with 2 states with time 1.0859233289957047 seconds
Training complete for GIVE2 with 9 states with time 0.21004998200805858 seconds
Training complete for GIVE3 with 10 states with time 0.26795192901045084 seconds
Training complete for GET with 6 states with time 0.13127426896244287 seconds
Training complete for PUTASIDE with 4 states with time 0.22753332502907142 seconds
Number of word models returned = 112
'19/04/2017 04:18:17 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:18:17 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:18:26 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5561797752808989
Total correct: 79 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *BOOK *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN *PEOPLE GO *HAVE                                         JOHN CAN GO CAN
   12: JOHN CAN *WHAT CAN                                            JOHN CAN GO CAN
   21: *MARY *VIDEOTAPE WONT *MARY *CAR *CAR *GO *EAT                JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *IX IX IX IX                                             JOHN LIKE IX IX IX
   28: JOHN *WHO IX IX IX                                            JOHN LIKE IX IX IX
   30: JOHN LIKE IX *LIKE IX                                         JOHN LIKE IX IX IX
   36: MARY *MARY *GIRL *GIVE *MARY *MARY                            MARY VEGETABLE KNOW IX LIKE CORN1
   40: *MARY *GIVE *CORN MARY *IX                                    JOHN IX THINK MARY LOVE
   43: JOHN *SHOULD BUY HOUSE                                        JOHN MUST BUY HOUSE
   50: *JOHN *SEE BUY CAR SHOULD                                     FUTURE JOHN BUY CAR SHOULD
   54: JOHN *JOHN *MARY BUY HOUSE                                    JOHN SHOULD NOT BUY HOUSE
   57: JOHN *MARY *IX *GIVE                                          JOHN DECIDE VISIT MARY
   67: JOHN *SOMETHING-ONE *IX BUY HOUSE                             JOHN FUTURE NOT BUY HOUSE
   71: JOHN *JOHN VISIT MARY                                         JOHN WILL VISIT MARY
   74: JOHN *MARY *IX *IX                                            JOHN NOT VISIT MARY
   77: *IX BLAME *IX                                                 ANN BLAME MARY
   84: *JOHN *ARRIVE *GO BOOK                                        IX-1P FIND SOMETHING-ONE BOOK
   89: JOHN *SOMETHING-ONE *IX *IX IX NEW *BREAK-DOWN                JOHN IX GIVE MAN IX NEW COAT
   90: *MARY *SOMETHING-ONE IX SOMETHING-ONE *MARY *CHOCOLATE        JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *IX IX *IX *IX BOOK                                      JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: *IX NEW CAR BREAK-DOWN                                        POSS NEW CAR BREAK-DOWN
  105: JOHN *SHOULD                                                  JOHN LEG
  107: *MARY *JOHN *HAVE *VISIT *MARY                                JOHN POSS FRIEND HAVE CANDY
  108: *JOHN *BOOK                                                   WOMAN ARRIVE
  113: *JOHN CAR BLUE *JOHN *HAVE                                    IX CAR BLUE SUE BUY
  119: *MARY *BUY1 *HAVE *HAVE *SUE                                  SUE BUY IX CAR BLUE
  122: JOHN *HOUSE BOOK                                              JOHN READ BOOK
  139: JOHN *BUY1 WHAT YESTERDAY *ARRIVE                             JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY *HOUSE BOOK                                JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *MARY *MARY                                              LOVE JOHN WHO
  167: JOHN *SOMETHING-ONE *MARY LOVE *VISIT                         JOHN IX SAY LOVE MARY
  171: *MARY *JOHN BLAME                                             JOHN MARY BLAME
  174: *GIVE1 *NEW GIVE1 *MARY *BLAME                                PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *SOMETHING-ONE BOY *GIVE1 TEACHER APPLE                       ALL BOY GIVE TEACHER APPLE
  189: *MARY *SOMETHING-ONE *JOHN BOX                                JOHN GIVE GIRL BOX
  193: JOHN *IX *JOHN BOX                                            JOHN GIVE GIRL BOX
  199: *JOHN CHOCOLATE *JOHN                                         LIKE CHOCOLATE WHO
  201: JOHN *GIVE *IX *JOHN BUY HOUSE                                JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:18:26 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:18:26 PM' - root - DEBUG - Please wait...
'19/04/2017 04:18:50 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:18:50 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, delta, right
Chosen Model Selector:  SelectorBIC
Training complete for JOHN with 10 states with time 20.71034435305046 seconds
Training complete for WRITE with 9 states with time 0.24120214802678674 seconds
Training complete for HOMEWORK with 8 states with time 0.2202069609775208 seconds
Training complete for IX-1P with 10 states with time 0.36655763204908 seconds
Training complete for SEE with 10 states with time 0.5319823719910346 seconds
Training complete for YESTERDAY with 10 states with time 0.5436003600480035 seconds
Training complete for IX with 7 states with time 3.606036084005609 seconds
Training complete for LOVE with 10 states with time 1.033718377002515 seconds
Training complete for MARY with 10 states with time 3.7257214940036647 seconds
Training complete for CAN with 10 states with time 1.5114393520052545 seconds
Training complete for GO with 10 states with time 0.8084764480008744 seconds
Training complete for GO1 with 10 states with time 0.3896439130185172 seconds
Training complete for FUTURE with 10 states with time 1.00351867696736 seconds
Training complete for GO2 with 5 states with time 0.09642024099593982 seconds
Training complete for PARTY with 7 states with time 0.16060804401058704 seconds
Training complete for FUTURE1 with 5 states with time 0.20824863901361823 seconds
Training complete for HIT with 7 states with time 0.15022402699105442 seconds
Training complete for BLAME with 10 states with time 0.3713376419618726 seconds
Training complete for FRED with 3 states with time 0.16293510101968423 seconds
Training complete for FISH with 4 states with time 0.226437708013691 seconds
Training complete for WONT with 8 states with time 0.27448690199526027 seconds
Training complete for EAT with 6 states with time 0.3084470889880322 seconds
Training complete for BUT with 10 states with time 0.22682813298888505 seconds
Training complete for CHICKEN with 7 states with time 0.2598962169722654 seconds
Training complete for VEGETABLE with 9 states with time 0.46582780801691115 seconds
Training complete for CHINA with 10 states with time 0.23893909202888608 seconds
Training complete for PEOPLE with 9 states with time 0.37240459996974096 seconds
Training complete for PREFER with 10 states with time 0.48164165497291833 seconds
Training complete for BROCCOLI with 7 states with time 0.2840525589999743 seconds
Training complete for LIKE with 9 states with time 0.7769438340328634 seconds
Training complete for LEAVE with 10 states with time 0.42689547303598374 seconds
Training complete for SAY with 3 states with time 0.22334822901757434 seconds
Training complete for BUY with 10 states with time 1.2658987769973464 seconds
Training complete for HOUSE with 10 states with time 0.9644633759744465 seconds
Training complete for KNOW with 3 states with time 0.26227356103481725 seconds
Training complete for CORN with 9 states with time 0.3761681309551932 seconds
Training complete for CORN1 with 3 states with time 0.3857986619696021 seconds
Training complete for THINK with 4 states with time 0.3098355489782989 seconds
Training complete for NOT with 10 states with time 0.7385266899946146 seconds
Training complete for PAST with 3 states with time 0.24081498599844053 seconds
Training complete for LIVE with 3 states with time 0.10732422099681571 seconds
Training complete for CHICAGO with 7 states with time 0.2361390870064497 seconds
Training complete for CAR with 10 states with time 1.3964898979756981 seconds
Training complete for SHOULD with 10 states with time 0.7001281770062633 seconds
Training complete for DECIDE with 7 states with time 0.22690299298847094 seconds
Training complete for VISIT with 10 states with time 0.9521209000376984 seconds
Training complete for MOVIE with 7 states with time 0.2507316810078919 seconds
Training complete for WANT with 7 states with time 0.22666715801460668 seconds
Training complete for SELL with 10 states with time 0.23779799998737872 seconds
Training complete for TOMORROW with 10 states with time 0.17713545699371025 seconds
Training complete for NEXT-WEEK with 5 states with time 0.10439793899422511 seconds
Training complete for NEW-YORK with 7 states with time 0.25057900097453967 seconds
Training complete for LAST-WEEK with 10 states with time 0.19620398001279682 seconds
Training complete for WILL with 5 states with time 0.21103632700396702 seconds
Training complete for FINISH with 10 states with time 0.34164255805080757 seconds
Training failed for ANN
Training complete for READ with 10 states with time 0.2571364580071531 seconds
Training complete for BOOK with 10 states with time 1.1345465399790555 seconds
Training complete for CHOCOLATE with 10 states with time 0.3233056869939901 seconds
Training complete for FIND with 2 states with time 0.04433719697408378 seconds
Training complete for SOMETHING-ONE with 10 states with time 0.8627917270059697 seconds
Training complete for POSS with 9 states with time 0.7104454939835705 seconds
Training complete for BROTHER with 10 states with time 0.2499732399592176 seconds
Training complete for ARRIVE with 10 states with time 1.2720202630152926 seconds
Training complete for HERE with 10 states with time 0.25436275597894564 seconds
Training complete for GIVE with 10 states with time 0.8279549510334618 seconds
Training complete for MAN with 10 states with time 0.27207697997801006 seconds
Training complete for NEW with 10 states with time 0.37263503804570064 seconds
Training complete for COAT with 10 states with time 0.2403045779792592 seconds
Training complete for WOMAN with 10 states with time 0.6278398020076565 seconds
Training complete for GIVE1 with 10 states with time 0.8832177959848195 seconds
Training complete for HAVE with 10 states with time 0.3323725840309635 seconds
Training complete for FRANK with 6 states with time 0.3365533860051073 seconds
Training complete for BREAK-DOWN with 7 states with time 0.35027212800923735 seconds
Training complete for SEARCH-FOR with 10 states with time 0.21454448002623394 seconds
Training complete for WHO with 10 states with time 2.0952555459807627 seconds
Training complete for WHAT with 10 states with time 1.9053399999975227 seconds
Training failed for LEG
Training complete for FRIEND with 8 states with time 0.1971287719788961 seconds
Training failed for CANDY
Training complete for BLUE with 6 states with time 0.2618080279789865 seconds
Training complete for SUE with 10 states with time 0.3533340410212986 seconds
Training complete for BUY1 with 10 states with time 0.4598334099864587 seconds
Training complete for STOLEN with 10 states with time 0.24844744603615254 seconds
Training complete for OLD with 2 states with time 0.156050022051204 seconds
Training complete for STUDENT with 10 states with time 0.26435728499200195 seconds
Training complete for VIDEOTAPE with 8 states with time 0.28292097500525415 seconds
Training complete for BORROW with 2 states with time 0.08800979796797037 seconds
Training complete for MOTHER with 10 states with time 0.23874146200250834 seconds
Training complete for POTATO with 5 states with time 0.19113031501183286 seconds
Training complete for TELL with 10 states with time 0.3182035659556277 seconds
Training complete for BILL with 9 states with time 0.48533425002824515 seconds
Training complete for THROW with 10 states with time 0.3073802890139632 seconds
Training complete for APPLE with 10 states with time 0.3537386119714938 seconds
Training complete for NAME with 7 states with time 0.1760067220311612 seconds
Training complete for SHOOT with 10 states with time 0.21267292596166953 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 0.21160022600088269 seconds
Training complete for GROUP with 4 states with time 0.15837613999610767 seconds
Training complete for JANA with 9 states with time 0.26126056496286765 seconds
Training complete for TOY1 with 9 states with time 0.21399170596851036 seconds
Training complete for MANY with 4 states with time 0.15092812501825392 seconds
Training complete for TOY with 4 states with time 0.20212525298120454 seconds
Training complete for ALL with 9 states with time 0.23983824404422194 seconds
Training complete for BOY with 9 states with time 0.2888123979791999 seconds
Training complete for TEACHER with 10 states with time 0.39052615297259763 seconds
Training complete for GIRL with 5 states with time 0.43234893400222063 seconds
Training complete for BOX with 10 states with time 0.541593581030611 seconds
Training complete for GIVE2 with 8 states with time 0.19698810897534713 seconds
Training complete for GIVE3 with 9 states with time 0.27252786402823403 seconds
Training complete for GET with 6 states with time 0.11500662099570036 seconds
Training complete for PUTASIDE with 4 states with time 0.20332829101243988 seconds
Number of word models returned = 112
'19/04/2017 04:20:10 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:20:10 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:20:20 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5168539325842697
Total correct: 86 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *NEW *ARRIVE                                             JOHN WRITE HOMEWORK
    7: JOHN *CAR *IX CAN                                             JOHN CAN GO CAN
   12: JOHN *WHAT *JOHN *HOUSE                                       JOHN CAN GO CAN
   21: JOHN *GIVE1 *JOHN *JOHN *HOUSE *CAR *FUTURE *MARY             JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *JOHN *LOVE IX *JOHN                                     JOHN LIKE IX IX IX
   28: JOHN *MARY IX *JOHN IX                                        JOHN LIKE IX IX IX
   30: JOHN *MARY *MARY IX IX                                        JOHN LIKE IX IX IX
   36: *JOHN *JOHN *IX IX *MARY *MARY                                MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *JOHN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: JOHN *JOHN BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *JOHN *FRANK BUY CAR *JOHN                                    FUTURE JOHN BUY CAR SHOULD
   54: JOHN *FUTURE *FUTURE BUY HOUSE                                JOHN SHOULD NOT BUY HOUSE
   57: *IX *JOHN *IX *IX                                             JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *MARY BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *IX *IX *IX                                               JOHN NOT VISIT MARY
   77: *JOHN BLAME *BLAME                                            ANN BLAME MARY
   84: *JOHN *ARRIVE *VISIT BOOK                                     IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY IX GIVE *WOMAN IX NEW *BREAK-DOWN                       JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX *IX *VIDEOTAPE                                JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN GIVE *WOMAN *WOMAN *JOHN BOOK                            JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *MARY                                                    JOHN LEG
  107: JOHN *IX *ARRIVE *IX *IX                                      JOHN POSS FRIEND HAVE CANDY
  108: *JOHN ARRIVE                                                  WOMAN ARRIVE
  113: IX CAR *IX *MARY *BOX                                         IX CAR BLUE SUE BUY
  119: *JOHN *BUY1 IX CAR *IX                                        SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: *IX *BUY1 WHAT *JOHN BOOK                                     JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *IX LOVE MARY                                         JOHN IX SAY LOVE MARY
  171: JOHN MARY BLAME                                               JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *IX *JOHN                                  PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN ARRIVE                                                   JOHN ARRIVE
  184: *IX *IX *GIVE1 TEACHER *IX                                    ALL BOY GIVE TEACHER APPLE
  189: JOHN *JOHN *JOHN BOX                                          JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE WHO                                             LIKE CHOCOLATE WHO
  201: JOHN *GIVE MARY *JOHN BUY HOUSE                               JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:20:20 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:20:20 PM' - root - DEBUG - Please wait...
'19/04/2017 04:20:45 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:20:45 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, delta, right
Chosen Model Selector:  SelectorDIC
Training complete for JOHN with 10 states with time 20.915108629968017 seconds
Training complete for WRITE with 9 states with time 1.7665048830094747 seconds
Training complete for HOMEWORK with 5 states with time 0.7975091860280372 seconds
Training complete for IX-1P with 10 states with time 2.1936031199875288 seconds
Training complete for SEE with 10 states with time 2.3068592980271205 seconds
Training complete for YESTERDAY with 10 states with time 2.2464684389997274 seconds
Training complete for IX with 9 states with time 5.185971917991992 seconds
Training complete for LOVE with 10 states with time 2.6770939480047673 seconds
Training complete for MARY with 10 states with time 5.432111181027722 seconds
Training complete for CAN with 10 states with time 3.3626529140165076 seconds
Training complete for GO with 10 states with time 2.6775259120040573 seconds
Training complete for GO1 with 10 states with time 2.2230527859646827 seconds
Training complete for FUTURE with 9 states with time 2.6872509680106305 seconds
Training complete for GO2 with 5 states with time 0.8479412799933925 seconds
Training complete for PARTY with 7 states with time 1.3219022519770078 seconds
Training complete for FUTURE1 with 5 states with time 0.7821037069661543 seconds
Training complete for HIT with 7 states with time 1.2886113339918666 seconds
Training complete for BLAME with 10 states with time 2.2760247830301523 seconds
Training complete for FRED with 3 states with time 0.42225146101554856 seconds
Training complete for FISH with 2 states with time 0.38556771900039166 seconds
Training complete for WONT with 8 states with time 1.734460513049271 seconds
Training complete for EAT with 6 states with time 1.1738580479868688 seconds
Training complete for BUT with 9 states with time 2.2809344919514842 seconds
Training complete for CHICKEN with 7 states with time 1.4227749080164358 seconds
Training complete for VEGETABLE with 2 states with time 1.3983812970109284 seconds
Training complete for CHINA with 10 states with time 2.2034554349957034 seconds
Training complete for PEOPLE with 10 states with time 2.0504011909943074 seconds
Training complete for PREFER with 8 states with time 2.1915489259990864 seconds
Training complete for BROCCOLI with 6 states with time 1.2791038160212338 seconds
Training complete for LIKE with 10 states with time 2.3242091339780018 seconds
Training complete for LEAVE with 4 states with time 2.1550332990009338 seconds
Training complete for SAY with 2 states with time 0.41111868497682735 seconds
Training complete for BUY with 10 states with time 2.739366397028789 seconds
Training complete for HOUSE with 10 states with time 2.5225565920118243 seconds
Training complete for KNOW with 2 states with time 0.40844437398482114 seconds
Training complete for CORN with 2 states with time 1.3565569359925576 seconds
Training complete for CORN1 with 2 states with time 0.3899925999576226 seconds
Training complete for THINK with 3 states with time 0.5815769240143709 seconds
Training complete for NOT with 6 states with time 2.3681475240155123 seconds
Training complete for PAST with 2 states with time 0.5782684830483049 seconds
Training complete for LIVE with 3 states with time 0.37733618897618726 seconds
Training complete for CHICAGO with 7 states with time 1.316785887000151 seconds
Training complete for CAR with 9 states with time 2.7353799620177597 seconds
Training complete for SHOULD with 10 states with time 2.3107930370024405 seconds
Training complete for DECIDE with 6 states with time 1.3275801069685258 seconds
Training complete for VISIT with 10 states with time 2.6080572809441946 seconds
Training complete for MOVIE with 7 states with time 1.2681310980115086 seconds
Training complete for WANT with 7 states with time 1.328239752969239 seconds
Training complete for SELL with 9 states with time 2.117147500975989 seconds
Training complete for TOMORROW with 9 states with time 2.0830508330254816 seconds
Training complete for NEXT-WEEK with 5 states with time 0.7977004490094259 seconds
Training complete for NEW-YORK with 8 states with time 1.5697471189778298 seconds
Training complete for LAST-WEEK with 10 states with time 2.04942460503662 seconds
Training complete for WILL with 5 states with time 0.8176540199783631 seconds
Training complete for FINISH with 10 states with time 2.088589505990967 seconds
Training failed for ANN
Training complete for READ with 10 states with time 2.1293014909606427 seconds
Training complete for BOOK with 10 states with time 2.781292959989514 seconds
Training complete for CHOCOLATE with 10 states with time 2.067351598001551 seconds
Training complete for FIND with 2 states with time 0.1891869449755177 seconds
Training complete for SOMETHING-ONE with 9 states with time 2.6390195380081423 seconds
Training complete for POSS with 4 states with time 0.7511807500268333 seconds
Training complete for BROTHER with 10 states with time 2.1659546309965663 seconds
Training complete for ARRIVE with 10 states with time 3.2514004909899086 seconds
Training complete for HERE with 10 states with time 2.29706657899078 seconds
Training complete for GIVE with 9 states with time 2.7147439219988883 seconds
Training complete for MAN with 3 states with time 2.3742694089887664 seconds
Training complete for NEW with 10 states with time 2.2007491220138036 seconds
Training complete for COAT with 8 states with time 2.089464736985974 seconds
Training complete for WOMAN with 10 states with time 2.5084485740517266 seconds
Training complete for GIVE1 with 8 states with time 2.749087780015543 seconds
Training complete for HAVE with 10 states with time 2.228594746964518 seconds
Training complete for FRANK with 6 states with time 1.2503466079942882 seconds
Training complete for BREAK-DOWN with 7 states with time 1.495511444984004 seconds
Training complete for SEARCH-FOR with 4 states with time 0.9161589050199836 seconds
Training complete for WHO with 10 states with time 3.793684661970474 seconds
Training complete for WHAT with 9 states with time 3.875886094989255 seconds
Training failed for LEG
Training complete for FRIEND with 7 states with time 1.6288419510237873 seconds
Training failed for CANDY
Training complete for BLUE with 6 states with time 1.3580872580059804 seconds
Training complete for SUE with 7 states with time 2.4469188970397227 seconds
Training complete for BUY1 with 9 states with time 2.6636245120316744 seconds
Training complete for STOLEN with 4 states with time 0.857595288020093 seconds
Training complete for OLD with 2 states with time 0.21923278499161825 seconds
Training complete for STUDENT with 10 states with time 2.035999935003929 seconds
Training complete for VIDEOTAPE with 7 states with time 1.6671339410240762 seconds
Training complete for BORROW with 2 states with time 0.19004935503471643 seconds
Training complete for MOTHER with 10 states with time 2.0601967109832913 seconds
Training complete for POTATO with 5 states with time 0.7947696560295299 seconds
Training complete for TELL with 2 states with time 2.2092946780030616 seconds
Training complete for BILL with 2 states with time 2.349925426999107 seconds
Training complete for THROW with 6 states with time 2.1908669699914753 seconds
Training complete for APPLE with 8 states with time 2.417541788017843 seconds
Training complete for NAME with 6 states with time 2.108295598998666 seconds
Training complete for SHOOT with 10 states with time 2.1186934020370245 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 2.3344167239847593 seconds
Training complete for GROUP with 4 states with time 0.6838737000362016 seconds
Training complete for JANA with 10 states with time 2.6776231749681756 seconds
Training complete for TOY1 with 8 states with time 2.1260278950212523 seconds
Training complete for MANY with 4 states with time 0.7920320970006287 seconds
Training complete for TOY with 4 states with time 0.7759125150041655 seconds
Training complete for ALL with 9 states with time 2.0137841020477936 seconds
Training complete for BOY with 9 states with time 1.9249552249675617 seconds
Training complete for TEACHER with 10 states with time 2.5416102280141786 seconds
Training complete for GIRL with 5 states with time 1.4177274260437116 seconds
Training complete for BOX with 10 states with time 2.53414286399493 seconds
Training complete for GIVE2 with 2 states with time 1.8187412630068138 seconds
Training complete for GIVE3 with 9 states with time 2.3588790689827874 seconds
Training complete for GET with 6 states with time 1.0734610960353166 seconds
Training complete for PUTASIDE with 4 states with time 0.6795309520093724 seconds
Number of word models returned = 112
'19/04/2017 04:24:31 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:24:31 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:24:42 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5280898876404494
Total correct: 84 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *NEW *GIVE1                                              JOHN WRITE HOMEWORK
    7: JOHN *CAR *IX CAN                                             JOHN CAN GO CAN
   12: JOHN *WHAT *WHAT *HOUSE                                       JOHN CAN GO CAN
   21: JOHN *GIVE1 *JOHN *JOHN *CAR *CAR *FUTURE *MARY               JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *JOHN *LOVE IX *JOHN                                     JOHN LIKE IX IX IX
   28: JOHN *MARY IX *JOHN IX                                        JOHN LIKE IX IX IX
   30: *IX *IX *MARY IX IX                                           JOHN LIKE IX IX IX
   36: *JOHN *JOHN *IX IX *MARY *MARY                                MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN *BILL *CORN MARY *IX                                     JOHN IX THINK MARY LOVE
   43: JOHN *JOHN BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *JOHN *FRANK BUY CAR *JOHN                                    FUTURE JOHN BUY CAR SHOULD
   54: JOHN *JOHN NOT BUY HOUSE                                      JOHN SHOULD NOT BUY HOUSE
   57: *IX *JOHN *IX *IX                                             JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *MARY BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *BILL *IX *IX                                             JOHN NOT VISIT MARY
   77: *JOHN BLAME *BLAME                                            ANN BLAME MARY
   84: *JOHN *ARRIVE *VISIT BOOK                                     IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *SOMETHING-ONE GIVE *WOMAN IX NEW *BREAK-DOWN           JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX *IX BOOK                                      JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN GIVE *WOMAN *WOMAN *JOHN BOOK                            JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *MARY                                                    JOHN LEG
  107: JOHN *IX *ARRIVE *MARY *JOHN                                  JOHN POSS FRIEND HAVE CANDY
  108: *JOHN ARRIVE                                                  WOMAN ARRIVE
  113: IX CAR *IX *MARY *BOX                                         IX CAR BLUE SUE BUY
  119: *JOHN *BUY1 IX CAR *IX                                        SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: *IX *BUY1 *CAR *JOHN BOOK                                     JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *IX LOVE MARY                                         JOHN IX SAY LOVE MARY
  171: JOHN MARY BLAME                                               JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *IX *JOHN                                  PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN ARRIVE                                                   JOHN ARRIVE
  184: *IX *IX *GIVE1 TEACHER *IX                                    ALL BOY GIVE TEACHER APPLE
  189: JOHN *JOHN *JOHN BOX                                          JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *JOHN *HOMEWORK WHO                                           LIKE CHOCOLATE WHO
  201: JOHN *GIVE MARY *JOHN BUY HOUSE                               JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:24:42 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:24:42 PM' - root - DEBUG - Please wait...
'19/04/2017 04:25:15 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:25:15 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta
Chosen Model Selector:  SelectorConstant
Training complete for JOHN with 3 states with time 1.3141498600016348 seconds
Training complete for WRITE with 3 states with time 0.016687156981788576 seconds
Training complete for HOMEWORK with 3 states with time 0.02429665601812303 seconds
Training complete for IX-1P with 3 states with time 0.025855301995761693 seconds
Training complete for SEE with 3 states with time 0.036145186983048916 seconds
Training complete for YESTERDAY with 3 states with time 0.038657878001686186 seconds
Training complete for IX with 3 states with time 0.3939290840062313 seconds
Training complete for LOVE with 3 states with time 0.05935735703678802 seconds
Training complete for MARY with 3 states with time 0.4725545570254326 seconds
Training complete for CAN with 3 states with time 0.06988752604229376 seconds
Training complete for GO with 3 states with time 0.07836747501278296 seconds
Training complete for GO1 with 3 states with time 0.02482537302421406 seconds
Training complete for FUTURE with 3 states with time 0.08976526599144563 seconds
Training complete for GO2 with 3 states with time 0.01414888899307698 seconds
Training complete for PARTY with 3 states with time 0.016070340003352612 seconds
Training complete for FUTURE1 with 3 states with time 0.01532173395389691 seconds
Training complete for HIT with 3 states with time 0.014806533989030868 seconds
Training complete for BLAME with 3 states with time 0.02729325700784102 seconds
Training complete for FRED with 3 states with time 0.013433624000754207 seconds
Training complete for FISH with 3 states with time 0.021924650005530566 seconds
Training complete for WONT with 3 states with time 0.020059961010701954 seconds
Training complete for EAT with 3 states with time 0.024240206985268742 seconds
Training complete for BUT with 3 states with time 0.01934632600750774 seconds
Training complete for CHICKEN with 3 states with time 0.01951870700577274 seconds
Training complete for VEGETABLE with 3 states with time 0.031751288974191993 seconds
Training complete for CHINA with 3 states with time 0.02017332601826638 seconds
Training complete for PEOPLE with 3 states with time 0.04429872095352039 seconds
Training complete for PREFER with 3 states with time 0.029736488999333233 seconds
Training complete for BROCCOLI with 3 states with time 0.021353950025513768 seconds
Training complete for LIKE with 3 states with time 0.03898203099379316 seconds
Training complete for LEAVE with 3 states with time 0.018541686004027724 seconds
Training complete for SAY with 3 states with time 0.016317566973157227 seconds
Training complete for BUY with 3 states with time 0.12686004594434053 seconds
Training complete for HOUSE with 3 states with time 0.11266486597014591 seconds
Training complete for KNOW with 3 states with time 0.022549993998836726 seconds
Training complete for CORN with 3 states with time 0.025336585997138172 seconds
Training complete for CORN1 with 3 states with time 0.02343884902074933 seconds
Training complete for THINK with 3 states with time 0.018757331010419875 seconds
Training complete for NOT with 3 states with time 0.03213498502736911 seconds
Training complete for PAST with 3 states with time 0.01463131100172177 seconds
Training complete for LIVE with 3 states with time 0.01359446597052738 seconds
Training complete for CHICAGO with 3 states with time 0.013927667983807623 seconds
Training complete for CAR with 3 states with time 0.06781151401810348 seconds
Training complete for SHOULD with 3 states with time 0.056301326025277376 seconds
Training complete for DECIDE with 3 states with time 0.018968811025843024 seconds
Training complete for VISIT with 3 states with time 0.05244906299049035 seconds
Training complete for MOVIE with 3 states with time 0.019109255052171648 seconds
Training complete for WANT with 3 states with time 0.019426834012847394 seconds
Training complete for SELL with 3 states with time 0.019464423996396363 seconds
Training complete for TOMORROW with 3 states with time 0.0167286399519071 seconds
Training complete for NEXT-WEEK with 3 states with time 0.016686920018400997 seconds
Training complete for NEW-YORK with 3 states with time 0.021925706998445094 seconds
Training complete for LAST-WEEK with 3 states with time 0.01850131497485563 seconds
Training complete for WILL with 3 states with time 0.020348221994936466 seconds
Training complete for FINISH with 3 states with time 0.039379888970870525 seconds
Training complete for ANN with 3 states with time 0.016564583987928927 seconds
Training complete for READ with 3 states with time 0.01789851300418377 seconds
Training complete for BOOK with 3 states with time 0.18641429004492238 seconds
Training complete for CHOCOLATE with 3 states with time 0.022158752020914108 seconds
Training complete for FIND with 3 states with time 0.013767000986263156 seconds
Training complete for SOMETHING-ONE with 3 states with time 0.049785896961111575 seconds
Training complete for POSS with 3 states with time 0.0578570649959147 seconds
Training complete for BROTHER with 3 states with time 0.017765111988410354 seconds
Training complete for ARRIVE with 3 states with time 0.05077784101013094 seconds
Training complete for HERE with 3 states with time 0.023578413005452603 seconds
Training complete for GIVE with 3 states with time 0.07321740197949111 seconds
Training complete for MAN with 3 states with time 0.02727372699882835 seconds
Training complete for NEW with 3 states with time 0.029988019028678536 seconds
Training complete for COAT with 3 states with time 0.020566517021507025 seconds
Training complete for WOMAN with 3 states with time 0.03789240698097274 seconds
Training complete for GIVE1 with 3 states with time 0.08104461000766605 seconds
Training complete for HAVE with 3 states with time 0.02894951100461185 seconds
Training complete for FRANK with 3 states with time 0.019255757972132415 seconds
Training complete for BREAK-DOWN with 3 states with time 0.022799541999120265 seconds
Training complete for SEARCH-FOR with 3 states with time 0.0186151159578003 seconds
Training complete for WHO with 3 states with time 0.15771760704228655 seconds
Training complete for WHAT with 3 states with time 0.1069426120375283 seconds
Training complete for LEG with 3 states with time 0.013999625982251018 seconds
Training complete for FRIEND with 3 states with time 0.014393833000212908 seconds
Training complete for CANDY with 3 states with time 0.013733141007833183 seconds
Training complete for BLUE with 3 states with time 0.020995115977711976 seconds
Training complete for SUE with 3 states with time 0.025226940982975066 seconds
Training complete for BUY1 with 3 states with time 0.043681534996721894 seconds
Training complete for STOLEN with 3 states with time 0.01817270298488438 seconds
Training complete for OLD with 3 states with time 0.01597718702396378 seconds
Training complete for STUDENT with 3 states with time 0.02288978500291705 seconds
Training complete for VIDEOTAPE with 3 states with time 0.025159035983961076 seconds
Training complete for BORROW with 3 states with time 0.013892086979467422 seconds
Training complete for MOTHER with 3 states with time 0.01836122403619811 seconds
Training complete for POTATO with 3 states with time 0.012843848031479865 seconds
Training complete for TELL with 3 states with time 0.02195474796462804 seconds
Training complete for BILL with 3 states with time 0.021011706034187227 seconds
Training complete for THROW with 3 states with time 0.039395559986587614 seconds
Training complete for APPLE with 3 states with time 0.029989629983901978 seconds
Training complete for NAME with 3 states with time 0.016886274970602244 seconds
Training complete for SHOOT with 3 states with time 0.018119752989150584 seconds
Training complete for SAY-1P with 3 states with time 0.01884485501796007 seconds
Training complete for SELF with 3 states with time 0.01798811199842021 seconds
Training complete for GROUP with 3 states with time 0.01621137000620365 seconds
Training complete for JANA with 3 states with time 0.017619160993490368 seconds
Training complete for TOY1 with 3 states with time 0.01586135197430849 seconds
Training complete for MANY with 3 states with time 0.012959486979525536 seconds
Training complete for TOY with 3 states with time 0.013637463969644159 seconds
Training complete for ALL with 3 states with time 0.01670073496643454 seconds
Training complete for BOY with 3 states with time 0.023711207963060588 seconds
Training complete for TEACHER with 3 states with time 0.04446614295011386 seconds
Training complete for GIRL with 3 states with time 0.02862191601889208 seconds
Training complete for BOX with 3 states with time 0.04745896201347932 seconds
Training complete for GIVE2 with 3 states with time 0.014445565990172327 seconds
Training complete for GIVE3 with 3 states with time 0.019067240005824715 seconds
Training complete for GET with 3 states with time 0.01452452503144741 seconds
Training complete for PUTASIDE with 3 states with time 0.015169364050962031 seconds
Number of word models returned = 112
'19/04/2017 04:25:30 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:25:30 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:25:39 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5674157303370787
Total correct: 77 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: *POSS WRITE HOMEWORK                                          JOHN WRITE HOMEWORK
    7: JOHN *PEOPLE *IX *ARRIVE                                      JOHN CAN GO CAN
   12: JOHN *HAVE *WHAT CAN                                          JOHN CAN GO CAN
   21: JOHN *NEW *SOMETHING-ONE *MARY *CAR *CAR *FUTURE *MARY        JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN LIKE IX *WHO IX                                          JOHN LIKE IX IX IX
   28: *IX *WHO IX *LIKE IX                                          JOHN LIKE IX IX IX
   30: JOHN LIKE *MARY *MARY *MARY                                   JOHN LIKE IX IX IX
   36: MARY *JOHN *IX *GIVE *IX *MARY                                MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN *MARY *CORN MARY *MARY                                   JOHN IX THINK MARY LOVE
   43: *FRANK *POSS BUY HOUSE                                        JOHN MUST BUY HOUSE
   50: *POSS *POSS BUY CAR *IX                                       FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *FUTURE BUY HOUSE                                 JOHN SHOULD NOT BUY HOUSE
   57: JOHN *JOHN *IX MARY                                           JOHN DECIDE VISIT MARY
   67: *TELL FUTURE *MARY BUY HOUSE                                  JOHN FUTURE NOT BUY HOUSE
   71: *IX *FUTURE *GO MARY                                          JOHN WILL VISIT MARY
   74: *IX *MARY *MARY MARY                                          JOHN NOT VISIT MARY
   77: *IX BLAME MARY                                                ANN BLAME MARY
   84: *IX *ARRIVE *HOMEWORK BOOK                                    IX-1P FIND SOMETHING-ONE BOOK
   89: JOHN IX *IX *IX IX NEW COAT                                   JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *SOMETHING-ONE IX *IX *MARY *CHOCOLATE                   JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: *IX *IX *WOMAN *WOMAN WOMAN BOOK                              JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: *FRANK *POSS                                                  JOHN LEG
  107: JOHN *JOHN *HAVE *GO *JOHN                                    JOHN POSS FRIEND HAVE CANDY
  108: *MARY *BOOK                                                   WOMAN ARRIVE
  113: *JOHN CAR *SUE *JOHN *BOX                                     IX CAR BLUE SUE BUY
  119: *MARY *BUY1 *CAR CAR *HAVE                                    SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: JOHN *BUY1 *BOX YESTERDAY BOOK                                JOHN BUY WHAT YESTERDAY BOOK
  142: *FRANK BUY YESTERDAY WHAT BOOK                                JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *MARY WHO                                                LOVE JOHN WHO
  167: *MARY *SOMETHING-ONE *MARY LOVE *LOVE                         JOHN IX SAY LOVE MARY
  171: *MARY *JOHN BLAME                                             JOHN MARY BLAME
  174: *CAR *GIVE3 GIVE1 *MARY *BLAME                                PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER APPLE                                  ALL BOY GIVE TEACHER APPLE
  189: JOHN *SOMETHING-ONE *YESTERDAY BOX                            JOHN GIVE GIRL BOX
  193: JOHN *SOMETHING-ONE *IX BOX                                   JOHN GIVE GIRL BOX
  199: *IX CHOCOLATE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *MAN *IX *IX BUY HOUSE                                   JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:25:39 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:25:39 PM' - root - DEBUG - Please wait...
'19/04/2017 04:26:14 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:26:14 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta
Chosen Model Selector:  SelectorCV
Training complete for JOHN with 2 states with time 37.46821124700364 seconds
Training complete for WRITE with 10 states with time 0.3063175920397043 seconds
Training complete for HOMEWORK with 7 states with time 0.31848352402448654 seconds
Training complete for IX-1P with 2 states with time 0.7573061850271188 seconds
Training complete for SEE with 3 states with time 1.2534267480368726 seconds
Training complete for YESTERDAY with 2 states with time 1.4350940180011094 seconds
Training complete for IX with 2 states with time 11.567578187969048 seconds
Training complete for LOVE with 3 states with time 2.2385139589896426 seconds
Training complete for MARY with 10 states with time 7.053140642994549 seconds
Training complete for CAN with 2 states with time 3.0928148100501858 seconds
Training complete for GO with 5 states with time 1.5522873539594002 seconds
Training complete for GO1 with 5 states with time 0.7564748050062917 seconds
Training complete for FUTURE with 2 states with time 2.034278154023923 seconds
Training complete for GO2 with 4 states with time 0.09516344504663721 seconds
Training complete for PARTY with 7 states with time 0.1506024760310538 seconds
Training complete for FUTURE1 with 5 states with time 0.19500118598807603 seconds
Training complete for HIT with 7 states with time 0.15306730096926913 seconds
Training complete for BLAME with 3 states with time 0.8606441069860011 seconds
Training complete for FRED with 4 states with time 0.1845569010474719 seconds
Training complete for FISH with 5 states with time 0.2335003290208988 seconds
Training complete for WONT with 2 states with time 0.42680548201315105 seconds
Training complete for EAT with 2 states with time 0.3589782670023851 seconds
Training complete for BUT with 8 states with time 0.20462630700785667 seconds
Training complete for CHICKEN with 7 states with time 0.23217466298956424 seconds
Training complete for VEGETABLE with 2 states with time 0.9354697109665722 seconds
Training complete for CHINA with 10 states with time 0.23807878501247615 seconds
Training complete for PEOPLE with 2 states with time 0.7021013650228269 seconds
Training complete for PREFER with 2 states with time 0.5351734000141732 seconds
Training complete for BROCCOLI with 8 states with time 0.26610376400640234 seconds
Training complete for LIKE with 2 states with time 1.0670933069777675 seconds
Training complete for LEAVE with 5 states with time 0.3802263729739934 seconds
Training complete for SAY with 5 states with time 0.2187619980541058 seconds
Training complete for BUY with 3 states with time 2.1349924050155096 seconds
Training complete for HOUSE with 2 states with time 1.4997657400090247 seconds
Training complete for KNOW with 2 states with time 0.33198484597960487 seconds
Training complete for CORN with 2 states with time 0.7333049069857225 seconds
Training complete for CORN1 with 6 states with time 0.2929998880135827 seconds
Training complete for THINK with 4 states with time 0.24893573398003355 seconds
Training complete for NOT with 2 states with time 1.5146526570315473 seconds
Training complete for PAST with 4 states with time 0.25075764500070363 seconds
Training complete for LIVE with 3 states with time 0.10690288303885609 seconds
Training complete for CHICAGO with 8 states with time 0.24728892400162295 seconds
Training complete for CAR with 3 states with time 2.7815514900139533 seconds
Training complete for SHOULD with 4 states with time 1.7284029619768262 seconds
Training complete for DECIDE with 7 states with time 0.26569873798871413 seconds
Training complete for VISIT with 2 states with time 1.6474759979755618 seconds
Training complete for MOVIE with 7 states with time 0.2633271759841591 seconds
Training complete for WANT with 8 states with time 0.27251369500299916 seconds
Training complete for SELL with 4 states with time 0.7334076360566542 seconds
Training complete for TOMORROW with 9 states with time 0.22555809695040807 seconds
Training complete for NEXT-WEEK with 5 states with time 0.13256430003093556 seconds
Training complete for NEW-YORK with 7 states with time 0.282266529975459 seconds
Training complete for LAST-WEEK with 9 states with time 0.20367180998437107 seconds
Training complete for WILL with 5 states with time 0.21268471895018592 seconds
Training complete for FINISH with 2 states with time 0.8241635910235345 seconds
Training complete for ANN with 3 states with time 0.23078897298546508 seconds
Training complete for READ with 2 states with time 0.6321968089905567 seconds
Training complete for BOOK with 2 states with time 2.292212492960971 seconds
Training complete for CHOCOLATE with 2 states with time 0.6489081369945779 seconds
Training complete for FIND with 2 states with time 0.049531549972016364 seconds
Training complete for SOMETHING-ONE with 3 states with time 1.4949275190010667 seconds
Training complete for POSS with 2 states with time 1.4993773679598235 seconds
Training complete for BROTHER with 10 states with time 0.2383884460432455 seconds
Training complete for ARRIVE with 2 states with time 2.108963812002912 seconds
Training complete for HERE with 3 states with time 0.3080999410012737 seconds
Training complete for GIVE with 3 states with time 1.4430867239716463 seconds
Training complete for MAN with 10 states with time 0.2864476180402562 seconds
Training complete for NEW with 4 states with time 1.06776629795786 seconds
Training complete for COAT with 10 states with time 0.33396688901120797 seconds
Training complete for WOMAN with 2 states with time 1.5939657929702662 seconds
Training complete for GIVE1 with 2 states with time 1.1831742179929279 seconds
Training complete for HAVE with 2 states with time 0.7363096589688212 seconds
Training complete for FRANK with 2 states with time 0.7291872089845128 seconds
Training complete for BREAK-DOWN with 2 states with time 0.6777126850211062 seconds
Training complete for SEARCH-FOR with 8 states with time 0.19993504899321124 seconds
Training complete for WHO with 3 states with time 2.5139103179681115 seconds
Training complete for WHAT with 9 states with time 3.8879407700151205 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 0.1931546870036982 seconds
Training complete for CANDY with 2 states with time 0.1875954660354182 seconds
Training complete for BLUE with 2 states with time 0.2962213179562241 seconds
Training complete for SUE with 2 states with time 0.47324066096916795 seconds
Training complete for BUY1 with 6 states with time 0.9029910039971583 seconds
Training complete for STOLEN with 8 states with time 0.27363246597815305 seconds
Training complete for OLD with 2 states with time 0.15544869896257296 seconds
Training complete for STUDENT with 2 states with time 0.40173295297427103 seconds
Training complete for VIDEOTAPE with 2 states with time 0.3823402400012128 seconds
Training complete for BORROW with 3 states with time 0.07502230699174106 seconds
Training complete for MOTHER with 4 states with time 0.41815661604050547 seconds
Training complete for POTATO with 5 states with time 0.21162528201239184 seconds
Training complete for TELL with 2 states with time 0.8009286249871366 seconds
Training complete for BILL with 2 states with time 0.8810971929924563 seconds
Training complete for THROW with 2 states with time 0.7496666699880734 seconds
Training complete for APPLE with 2 states with time 0.7471346860402264 seconds
Training complete for NAME with 10 states with time 0.1807032700162381 seconds
Training complete for SHOOT with 10 states with time 0.20272726099938154 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 0.2139687390299514 seconds
Training complete for GROUP with 5 states with time 0.16517761896830052 seconds
Training complete for JANA with 10 states with time 0.2386192039703019 seconds
Training complete for TOY1 with 9 states with time 0.20010439096949995 seconds
Training complete for MANY with 4 states with time 0.15967108501354232 seconds
Training complete for TOY with 4 states with time 0.20639144198503345 seconds
Training complete for ALL with 9 states with time 0.24444016604684293 seconds
Training complete for BOY with 4 states with time 0.3975256760022603 seconds
Training complete for TEACHER with 4 states with time 0.7721910740365274 seconds
Training complete for GIRL with 2 states with time 0.42326753097586334 seconds
Training complete for BOX with 2 states with time 0.9927291820058599 seconds
Training complete for GIVE2 with 9 states with time 0.2228577909991145 seconds
Training complete for GIVE3 with 10 states with time 0.24527957796817645 seconds
Training complete for GET with 7 states with time 0.1149324580328539 seconds
Training complete for PUTASIDE with 4 states with time 0.19080716697499156 seconds
Number of word models returned = 112
'19/04/2017 04:28:33 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:28:33 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:28:43 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5056179775280899
Total correct: 88 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *BOOK *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN *HAVE GO *HAVE                                           JOHN CAN GO CAN
   12: JOHN CAN *CAN CAN                                             JOHN CAN GO CAN
   21: JOHN *NEW *SOMETHING-ONE *MARY *GIVE1 *CAR *VISIT *VISIT      JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: *MARY *MARY IX *TELL IX                                       JOHN LIKE IX IX IX
   28: JOHN *TELL IX *LIKE IX                                        JOHN LIKE IX IX IX
   30: *IX LIKE IX *LIKE IX                                          JOHN LIKE IX IX IX
   36: MARY *JOHN *SOMETHING-ONE IX *IX *MARY                        MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *CORN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: JOHN *POSS BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *POSS *SEE BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *MARY BUY HOUSE                                   JOHN SHOULD NOT BUY HOUSE
   57: *IX *JOHN VISIT *IX                                           JOHN DECIDE VISIT MARY
   67: JOHN *POSS NOT BUY HOUSE                                      JOHN FUTURE NOT BUY HOUSE
   71: JOHN *JOHN VISIT MARY                                         JOHN WILL VISIT MARY
   74: JOHN *MARY VISIT MARY                                         JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *ARRIVE SOMETHING-ONE BOOK                              IX-1P FIND SOMETHING-ONE BOOK
   89: JOHN *SOMETHING-ONE *IX *IX IX NEW *BREAK-DOWN                JOHN IX GIVE MAN IX NEW COAT
   90: *MARY *SOMETHING-ONE *SOMETHING-ONE SOMETHING-ONE WOMAN BOOK  JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *GIVE1 *WOMAN *WOMAN WOMAN BOOK                          JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *POSS                                                    JOHN LEG
  107: *MARY *JOHN *HAVE HAVE *MARY                                  JOHN POSS FRIEND HAVE CANDY
  108: *JOHN *JOHN                                                   WOMAN ARRIVE
  113: *JOHN CAR *GO *MARY *BOX                                      IX CAR BLUE SUE BUY
  119: *MARY *BUY1 *GO *HAVE *GO                                     SUE BUY IX CAR BLUE
  122: JOHN *HOUSE BOOK                                              JOHN READ BOOK
  139: JOHN *LOVE WHAT YESTERDAY BOOK                                JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN *SOMETHING-ONE *VISIT LOVE *LOVE                         JOHN IX SAY LOVE MARY
  171: *MARY *JOHN BLAME                                             JOHN MARY BLAME
  174: *GIVE1 *GIVE1 GIVE1 *APPLE *VISIT                             PEOPLE GROUP GIVE1 JANA TOY
  181: *SUE *BOX                                                     JOHN ARRIVE
  184: *SOMETHING-ONE BOY *GIVE1 TEACHER APPLE                       ALL BOY GIVE TEACHER APPLE
  189: JOHN *SOMETHING-ONE *VISIT BOX                                JOHN GIVE GIRL BOX
  193: *IX *GIVE1 *JOHN BOX                                          JOHN GIVE GIRL BOX
  199: *JOHN CHOCOLATE *MARY                                         LIKE CHOCOLATE WHO
  201: JOHN *MARY *WOMAN *JOHN BUY HOUSE                             JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:28:43 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:28:43 PM' - root - DEBUG - Please wait...
'19/04/2017 04:29:16 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:29:16 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta
Chosen Model Selector:  SelectorBIC
Training complete for JOHN with 8 states with time 19.498748557001818 seconds
Training complete for WRITE with 10 states with time 0.24067945702699944 seconds
Training complete for HOMEWORK with 7 states with time 0.211702897970099 seconds
Training complete for IX-1P with 9 states with time 0.33048210304696113 seconds
Training complete for SEE with 10 states with time 0.46640617796219885 seconds
Training complete for YESTERDAY with 10 states with time 0.5175562239601277 seconds
Training complete for IX with 10 states with time 5.0018384929862805 seconds
Training complete for LOVE with 10 states with time 1.122348412987776 seconds
Training complete for MARY with 9 states with time 4.009331403998658 seconds
Training complete for CAN with 10 states with time 1.2549251629970968 seconds
Training complete for GO with 9 states with time 0.8336215000017546 seconds
Training complete for GO1 with 10 states with time 0.3194137779646553 seconds
Training complete for FUTURE with 10 states with time 1.1517629470326938 seconds
Training complete for GO2 with 4 states with time 0.08293535403208807 seconds
Training complete for PARTY with 7 states with time 0.15596981503767893 seconds
Training complete for FUTURE1 with 5 states with time 0.19126966898329556 seconds
Training complete for HIT with 7 states with time 0.1518220269936137 seconds
Training complete for BLAME with 10 states with time 0.3335758169996552 seconds
Training complete for FRED with 4 states with time 0.15440018201479688 seconds
Training complete for FISH with 5 states with time 0.22576964600011706 seconds
Training complete for WONT with 8 states with time 0.23866902402369305 seconds
Training complete for EAT with 6 states with time 0.2784502750146203 seconds
Training complete for BUT with 8 states with time 0.22035496402531862 seconds
Training complete for CHICKEN with 7 states with time 0.23804770899005234 seconds
Training complete for VEGETABLE with 10 states with time 0.5240675630047917 seconds
Training complete for CHINA with 10 states with time 0.21008430403890088 seconds
Training complete for PEOPLE with 10 states with time 0.3051419130060822 seconds
Training complete for PREFER with 10 states with time 0.35166143596870825 seconds
Training complete for BROCCOLI with 8 states with time 0.269013982033357 seconds
Training complete for LIKE with 9 states with time 0.6069073299877346 seconds
Training complete for LEAVE with 10 states with time 0.23081280203768983 seconds
Training complete for SAY with 5 states with time 0.1974837080342695 seconds
Training complete for BUY with 10 states with time 1.2610056080156937 seconds
Training complete for HOUSE with 10 states with time 0.7721955889719538 seconds
Training complete for KNOW with 3 states with time 0.23131733504123986 seconds
Training complete for CORN with 6 states with time 0.3396445900434628 seconds
Training complete for CORN1 with 6 states with time 0.2499590779771097 seconds
Training complete for THINK with 4 states with time 0.2089827639865689 seconds
Training complete for NOT with 10 states with time 0.5323259179713205 seconds
Training complete for PAST with 4 states with time 0.18611399800283834 seconds
Training complete for LIVE with 3 states with time 0.0784437190159224 seconds
Training complete for CHICAGO with 8 states with time 0.18029787798877805 seconds
Training complete for CAR with 10 states with time 1.1273083710111678 seconds
Training complete for SHOULD with 10 states with time 0.6064107630518265 seconds
Training complete for DECIDE with 7 states with time 0.2435917580150999 seconds
Training complete for VISIT with 10 states with time 0.7618007010314614 seconds
Training complete for MOVIE with 7 states with time 0.2298589320271276 seconds
Training complete for WANT with 8 states with time 0.21232478698948398 seconds
Training complete for SELL with 10 states with time 0.2525780239957385 seconds
Training complete for TOMORROW with 9 states with time 0.19885714299743995 seconds
Training complete for NEXT-WEEK with 5 states with time 0.1024041460477747 seconds
Training complete for NEW-YORK with 7 states with time 0.22565036703599617 seconds
Training complete for LAST-WEEK with 9 states with time 0.19484522397397086 seconds
Training complete for WILL with 5 states with time 0.20372792100533843 seconds
Training complete for FINISH with 9 states with time 0.31739190203370526 seconds
Training complete for ANN with 3 states with time 0.19040531205246225 seconds
Training complete for READ with 10 states with time 0.2341797100380063 seconds
Training complete for BOOK with 10 states with time 1.08400181500474 seconds
Training complete for CHOCOLATE with 10 states with time 0.30543446994852275 seconds
Training complete for FIND with 2 states with time 0.04033640096895397 seconds
Training complete for SOMETHING-ONE with 10 states with time 0.6842083549709059 seconds
Training complete for POSS with 8 states with time 0.6637577690416947 seconds
Training complete for BROTHER with 10 states with time 0.22568665503058583 seconds
Training complete for ARRIVE with 10 states with time 1.1243676309823059 seconds
Training complete for HERE with 10 states with time 0.2562049509724602 seconds
Training complete for GIVE with 10 states with time 0.707208368985448 seconds
Training complete for MAN with 10 states with time 0.26039097498869523 seconds
Training complete for NEW with 10 states with time 0.406897803011816 seconds
Training complete for COAT with 10 states with time 0.23943309800233692 seconds
Training complete for WOMAN with 8 states with time 0.6354766529984772 seconds
Training complete for GIVE1 with 10 states with time 0.653636981965974 seconds
Training complete for HAVE with 10 states with time 0.3031484190141782 seconds
Training complete for FRANK with 10 states with time 0.3061029910459183 seconds
Training complete for BREAK-DOWN with 8 states with time 0.3284392369678244 seconds
Training complete for SEARCH-FOR with 8 states with time 0.20449110900517553 seconds
Training complete for WHO with 10 states with time 1.4666300810058601 seconds
Training complete for WHAT with 10 states with time 1.9176676840288565 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 0.19319032196654007 seconds
Training complete for CANDY with 2 states with time 0.18391877302201465 seconds
Training complete for BLUE with 6 states with time 0.2605220800032839 seconds
Training complete for SUE with 10 states with time 0.29318072099704295 seconds
Training complete for BUY1 with 10 states with time 0.39891143201384693 seconds
Training complete for STOLEN with 8 states with time 0.2592514370335266 seconds
Training complete for OLD with 2 states with time 0.15196996397571638 seconds
Training complete for STUDENT with 10 states with time 0.25635695696109906 seconds
Training complete for VIDEOTAPE with 9 states with time 0.24099758896045387 seconds
Training complete for BORROW with 3 states with time 0.08269753603963181 seconds
Training complete for MOTHER with 9 states with time 0.24546658695908263 seconds
Training complete for POTATO with 5 states with time 0.17814539599930868 seconds
Training complete for TELL with 10 states with time 0.2923741169506684 seconds
Training complete for BILL with 10 states with time 0.4139093929552473 seconds
Training complete for THROW with 10 states with time 0.33020518999546766 seconds
Training complete for APPLE with 10 states with time 0.32140590000199154 seconds
Training complete for NAME with 7 states with time 0.17103022302035242 seconds
Training complete for SHOOT with 10 states with time 0.19482887396588922 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 0.22598725999705493 seconds
Training complete for GROUP with 5 states with time 0.1619779400061816 seconds
Training complete for JANA with 10 states with time 0.2442140849889256 seconds
Training complete for TOY1 with 9 states with time 0.1978721339837648 seconds
Training complete for MANY with 4 states with time 0.1479921360150911 seconds
Training complete for TOY with 4 states with time 0.20119457400869578 seconds
Training complete for ALL with 9 states with time 0.23310567502630875 seconds
Training complete for BOY with 10 states with time 0.2619186859810725 seconds
Training complete for TEACHER with 10 states with time 0.3685434330254793 seconds
Training complete for GIRL with 10 states with time 0.4634284629719332 seconds
Training complete for BOX with 10 states with time 0.458361542026978 seconds
Training complete for GIVE2 with 9 states with time 0.18565346096875146 seconds
Training complete for GIVE3 with 10 states with time 0.26463188201887533 seconds
Training complete for GET with 7 states with time 0.12167695496464148 seconds
Training complete for PUTASIDE with 4 states with time 0.20172363799065351 seconds
Number of word models returned = 112
'19/04/2017 04:30:34 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:30:34 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:30:44 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5168539325842697
Total correct: 86 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN *NEW *ARRIVE                                             JOHN WRITE HOMEWORK
    7: JOHN *JOHN GO CAN                                             JOHN CAN GO CAN
   12: JOHN CAN *JOHN CAN                                            JOHN CAN GO CAN
   21: JOHN *JOHN *JOHN *JOHN *JOHN *CAR *FUTURE *FUTURE             JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *MARY *LOVE IX IX                                        JOHN LIKE IX IX IX
   28: JOHN *MARY IX *JOHN IX                                        JOHN LIKE IX IX IX
   30: *IX *MARY *MARY *MARY IX                                      JOHN LIKE IX IX IX
   36: MARY *JOHN *IX IX *GO *MARY                                   MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN *MARY *CORN MARY *MARY                                   JOHN IX THINK MARY LOVE
   43: JOHN *JOHN BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *JOHN JOHN BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN *FUTURE *FUTURE BUY HOUSE                                JOHN SHOULD NOT BUY HOUSE
   57: JOHN *JOHN *IX MARY                                           JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *JOHN BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *MARY *MARY *IX                                           JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *JOHN *GO BOOK                                          IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *JOHN *WOMAN *WOMAN IX *ARRIVE *ARRIVE                  JOHN IX GIVE MAN IX NEW COAT
   90: *MARY *IX IX *IX WOMAN BOOK                                   JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *WOMAN IX *IX *IX BOOK                                   JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *FRANK                                                   JOHN LEG
  107: JOHN *IX *JOHN *MARY *MARY                                    JOHN POSS FRIEND HAVE CANDY
  108: *JOHN ARRIVE                                                  WOMAN ARRIVE
  113: IX CAR *IX *JOHN *BOX                                         IX CAR BLUE SUE BUY
  119: *MARY *BUY1 IX *JOHN *GO                                      SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: *IX *BUY1 WHAT *JOHN BOOK                                     JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *VISIT LOVE MARY                                      JOHN IX SAY LOVE MARY
  171: JOHN *IX BLAME                                                JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *IX *JOHN                                  PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER *GO                                    ALL BOY GIVE TEACHER APPLE
  189: JOHN *IX *VISIT BOX                                           JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *FUTURE *IX *WOMAN BUY HOUSE                             JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:30:44 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:30:44 PM' - root - DEBUG - Please wait...
'19/04/2017 04:31:17 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:31:17 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, delta
Chosen Model Selector:  SelectorDIC
Training complete for JOHN with 10 states with time 20.71137031802209 seconds
Training complete for WRITE with 9 states with time 2.003733880992513 seconds
Training complete for HOMEWORK with 5 states with time 0.789747424016241 seconds
Training complete for IX-1P with 9 states with time 1.9214003499946557 seconds
Training complete for SEE with 10 states with time 2.2486835979507305 seconds
Training complete for YESTERDAY with 10 states with time 2.1711161520215683 seconds
Training complete for IX with 10 states with time 6.500173837004695 seconds
Training complete for LOVE with 10 states with time 2.76336075499421 seconds
Training complete for MARY with 10 states with time 5.529476735042408 seconds
Training complete for CAN with 9 states with time 2.8416145230294205 seconds
Training complete for GO with 10 states with time 2.544298955996055 seconds
Training complete for GO1 with 10 states with time 2.0406946989824064 seconds
Training complete for FUTURE with 9 states with time 2.788481496972963 seconds
Training complete for GO2 with 4 states with time 0.5736047760001384 seconds
Training complete for PARTY with 7 states with time 1.3133778799674474 seconds
Training complete for FUTURE1 with 5 states with time 0.7919438069802709 seconds
Training complete for HIT with 7 states with time 1.312512672971934 seconds
Training complete for BLAME with 10 states with time 2.049008928996045 seconds
Training complete for FRED with 4 states with time 0.6176823460264131 seconds
Training complete for FISH with 3 states with time 0.8480152140255086 seconds
Training complete for WONT with 8 states with time 1.585352578025777 seconds
Training complete for EAT with 6 states with time 1.091316452017054 seconds
Training complete for BUT with 8 states with time 1.6948725729598664 seconds
Training complete for CHICKEN with 7 states with time 1.5131563440081663 seconds
Training complete for VEGETABLE with 2 states with time 2.427814728987869 seconds
Training complete for CHINA with 9 states with time 2.1015515809995122 seconds
Training complete for PEOPLE with 10 states with time 2.3336672440054826 seconds
Training complete for PREFER with 10 states with time 2.3925371779478155 seconds
Training complete for BROCCOLI with 8 states with time 1.6492847879999317 seconds
Training complete for LIKE with 7 states with time 1.5954338410519995 seconds
Training complete for LEAVE with 6 states with time 2.174909384979401 seconds
Training complete for SAY with 2 states with time 0.8267210319754668 seconds
Training complete for BUY with 10 states with time 2.9274559099576436 seconds
Training complete for HOUSE with 10 states with time 2.531589566031471 seconds
Training complete for KNOW with 2 states with time 0.39487305999500677 seconds
Training complete for CORN with 2 states with time 1.3955983910127543 seconds
Training complete for CORN1 with 2 states with time 1.0572489699698053 seconds
Training complete for THINK with 3 states with time 0.6155579659971409 seconds
Training complete for NOT with 10 states with time 2.3539261530386284 seconds
Training complete for PAST with 2 states with time 0.5841707930085249 seconds
Training complete for LIVE with 3 states with time 0.39552030799677595 seconds
Training complete for CHICAGO with 8 states with time 1.5789023149991408 seconds
Training complete for CAR with 10 states with time 2.7754531920072623 seconds
Training complete for SHOULD with 10 states with time 2.3709386810078286 seconds
Training complete for DECIDE with 7 states with time 1.333057829993777 seconds
Training complete for VISIT with 10 states with time 2.457372011966072 seconds
Training complete for MOVIE with 7 states with time 1.3266872449894436 seconds
Training complete for WANT with 8 states with time 1.5747838850365952 seconds
Training complete for SELL with 10 states with time 2.167359662009403 seconds
Training complete for TOMORROW with 9 states with time 1.8642114070244133 seconds
Training complete for NEXT-WEEK with 5 states with time 0.8113263470004313 seconds
Training complete for NEW-YORK with 7 states with time 1.4072640939848498 seconds
Training complete for LAST-WEEK with 9 states with time 2.0686108240042813 seconds
Training complete for WILL with 5 states with time 0.9199641140294261 seconds
Training complete for FINISH with 9 states with time 2.3973801930551417 seconds
Training complete for ANN with 2 states with time 0.4113675659755245 seconds
Training complete for READ with 10 states with time 2.084120303974487 seconds
Training complete for BOOK with 7 states with time 3.244242214015685 seconds
Training complete for CHOCOLATE with 9 states with time 2.2263400509837084 seconds
Training complete for FIND with 2 states with time 0.21394919004524127 seconds
Training complete for SOMETHING-ONE with 10 states with time 3.023854418017436 seconds
Training complete for POSS with 8 states with time 3.0785443340428174 seconds
Training complete for BROTHER with 10 states with time 2.048772521025967 seconds
Training complete for ARRIVE with 10 states with time 3.172345280996524 seconds
Training complete for HERE with 8 states with time 2.594686088967137 seconds
Training complete for GIVE with 2 states with time 2.6131814920227043 seconds
Training complete for MAN with 3 states with time 2.1903140320209786 seconds
Training complete for NEW with 10 states with time 2.0867170420242473 seconds
Training complete for COAT with 10 states with time 1.940625207964331 seconds
Training complete for WOMAN with 10 states with time 2.4163200489711016 seconds
Training complete for GIVE1 with 10 states with time 2.4357481750193983 seconds
Training complete for HAVE with 9 states with time 1.9649712549871765 seconds
Training complete for FRANK with 8 states with time 2.1807750329608098 seconds
Training complete for BREAK-DOWN with 8 states with time 1.5845368179725483 seconds
Training complete for SEARCH-FOR with 7 states with time 1.5853660719585605 seconds
Training complete for WHO with 9 states with time 3.165093160001561 seconds
Training complete for WHAT with 8 states with time 3.6593240589718334 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 1.0703110810136423 seconds
Training complete for CANDY with 2 states with time 0.21470586099894717 seconds
Training complete for BLUE with 6 states with time 1.1156286759651266 seconds
Training complete for SUE with 10 states with time 2.2248353240429424 seconds
Training complete for BUY1 with 10 states with time 2.2963331639766693 seconds
Training complete for STOLEN with 8 states with time 1.7856148880091496 seconds
Training complete for OLD with 2 states with time 0.21575038897572085 seconds
Training complete for STUDENT with 10 states with time 1.973884552018717 seconds
Training complete for VIDEOTAPE with 6 states with time 1.0121773550054058 seconds
Training complete for BORROW with 3 states with time 0.404708196001593 seconds
Training complete for MOTHER with 8 states with time 1.916219837963581 seconds
Training complete for POTATO with 5 states with time 0.7958660369622521 seconds
Training complete for TELL with 2 states with time 2.1328241880401038 seconds
Training complete for BILL with 2 states with time 2.300909679965116 seconds
Training complete for THROW with 10 states with time 2.951868198986631 seconds
Training complete for APPLE with 8 states with time 2.1415933319949545 seconds
Training complete for NAME with 6 states with time 2.4109825500054285 seconds
Training complete for SHOOT with 10 states with time 2.1930000970023684 seconds
Training failed for SAY-1P
Training complete for SELF with 8 states with time 3.0751434600097127 seconds
Training complete for GROUP with 5 states with time 1.1053848100127652 seconds
Training complete for JANA with 8 states with time 2.892317092977464 seconds
Training complete for TOY1 with 8 states with time 2.007918146031443 seconds
Training complete for MANY with 4 states with time 0.7034717000206001 seconds
Training complete for TOY with 4 states with time 0.7800559970200993 seconds
Training complete for ALL with 9 states with time 2.116772552020848 seconds
Training complete for BOY with 10 states with time 2.2930470900028013 seconds
Training complete for TEACHER with 9 states with time 2.519809607998468 seconds
Training complete for GIRL with 6 states with time 1.3839722520206124 seconds
Training complete for BOX with 10 states with time 2.3779051330056973 seconds
Training complete for GIVE2 with 2 states with time 2.0698738539940678 seconds
Training complete for GIVE3 with 10 states with time 2.1810177129809745 seconds
Training complete for GET with 7 states with time 1.3667291610036045 seconds
Training complete for PUTASIDE with 4 states with time 0.6125973380403593 seconds
Number of word models returned = 112
'19/04/2017 04:35:14 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:35:14 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:35:25 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.4887640449438202
Total correct: 91 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN WRITE *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN CAN GO CAN                                               JOHN CAN GO CAN
   12: JOHN *WHAT *JOHN CAN                                          JOHN CAN GO CAN
   21: JOHN *JOHN *JOHN *JOHN *CAR *CAR *FUTURE *FUTURE              JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN LIKE *LOVE IX IX                                         JOHN LIKE IX IX IX
   28: JOHN *MARY IX *MARY IX                                        JOHN LIKE IX IX IX
   30: *IX LIKE *MARY IX IX                                          JOHN LIKE IX IX IX
   36: MARY *JOHN *IX *GIVE *MARY *JOHN                              MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *CORN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: JOHN *FUTURE BUY HOUSE                                        JOHN MUST BUY HOUSE
   50: *JOHN JOHN BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *FUTURE BUY HOUSE                                 JOHN SHOULD NOT BUY HOUSE
   57: JOHN *JOHN *IX *IX                                            JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *FUTURE BUY HOUSE                                 JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *MARY *MARY *IX                                           JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *JOHN *JOHN BOOK                                        IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *POSS *IX *IX IX *ARRIVE *BOOK                          JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX *IX BOOK                                      JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *IX IX *IX *IX BOOK                                      JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *FRANK                                                   JOHN LEG
  107: JOHN *IX *JOHN *IX *JOHN                                      JOHN POSS FRIEND HAVE CANDY
  108: *JOHN ARRIVE                                                  WOMAN ARRIVE
  113: IX CAR *IX *MARY *BOX                                         IX CAR BLUE SUE BUY
  119: *JOHN *BUY1 IX *JOHN *JOHN                                    SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: *IX *BUY1 WHAT *JOHN BOOK                                     JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *VISIT LOVE MARY                                      JOHN IX SAY LOVE MARY
  171: JOHN MARY BLAME                                               JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *IX *JOHN                                  PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER *GO                                    ALL BOY GIVE TEACHER APPLE
  189: JOHN *IX *VISIT BOX                                           JOHN GIVE GIRL BOX
  193: JOHN *IX *IX BOX                                              JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *MAN *IX *JOHN BUY HOUSE                                 JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:35:25 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:35:25 PM' - root - DEBUG - Please wait...
'19/04/2017 04:35:58 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:35:58 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, right
Chosen Model Selector:  SelectorConstant
Training complete for JOHN with 3 states with time 0.9074882590211928 seconds
Training complete for WRITE with 3 states with time 0.0172084360383451 seconds
Training complete for HOMEWORK with 3 states with time 0.020342222996987402 seconds
Training complete for IX-1P with 3 states with time 0.030424889991991222 seconds
Training complete for SEE with 3 states with time 0.031219888012856245 seconds
Training complete for YESTERDAY with 3 states with time 0.035436748003121465 seconds
Training complete for IX with 3 states with time 0.4326774649671279 seconds
Training complete for LOVE with 3 states with time 0.08882115903543308 seconds
Training complete for MARY with 3 states with time 0.25653404695913196 seconds
Training complete for CAN with 3 states with time 0.12169136799639091 seconds
Training complete for GO with 3 states with time 0.0430416269809939 seconds
Training complete for GO1 with 3 states with time 0.030321827973239124 seconds
Training complete for FUTURE with 3 states with time 0.11574990401277319 seconds
Training complete for GO2 with 3 states with time 0.015640044992323965 seconds
Training complete for PARTY with 3 states with time 0.016962045978289098 seconds
Training complete for FUTURE1 with 3 states with time 0.015226995048578829 seconds
Training complete for HIT with 3 states with time 0.014712914009578526 seconds
Training complete for BLAME with 3 states with time 0.02634468802716583 seconds
Training complete for FRED with 3 states with time 0.015583426982630044 seconds
Training complete for FISH with 3 states with time 0.016114310012198985 seconds
Training complete for WONT with 3 states with time 0.020306901016738266 seconds
Training complete for EAT with 3 states with time 0.025910422031302005 seconds
Training complete for BUT with 3 states with time 0.018264274985995144 seconds
Training complete for CHICKEN with 3 states with time 0.0192035689833574 seconds
Training complete for VEGETABLE with 3 states with time 0.027601697016507387 seconds
Training complete for CHINA with 3 states with time 0.02124288398772478 seconds
Training complete for PEOPLE with 3 states with time 0.027586582000367343 seconds
Training complete for PREFER with 3 states with time 0.029503072961233556 seconds
Training complete for BROCCOLI with 3 states with time 0.0216623890446499 seconds
Training complete for LIKE with 3 states with time 0.04091390303801745 seconds
Training complete for LEAVE with 3 states with time 0.017638541001360863 seconds
Training complete for SAY with 3 states with time 0.019576541031710804 seconds
Training complete for BUY with 3 states with time 0.12440522201359272 seconds
Training complete for HOUSE with 3 states with time 0.06974549102596939 seconds
Training complete for KNOW with 3 states with time 0.02070221700705588 seconds
Training complete for CORN with 3 states with time 0.024660991970449686 seconds
Training complete for CORN1 with 3 states with time 0.01998547400580719 seconds
Training complete for THINK with 3 states with time 0.01586388604482636 seconds
Training complete for NOT with 3 states with time 0.03380892699351534 seconds
Training complete for PAST with 3 states with time 0.015180273039732128 seconds
Training complete for LIVE with 3 states with time 0.016432401025667787 seconds
Training complete for CHICAGO with 3 states with time 0.015132202999666333 seconds
Training complete for CAR with 3 states with time 0.12110639299498871 seconds
Training complete for SHOULD with 3 states with time 0.03822277102153748 seconds
Training complete for DECIDE with 3 states with time 0.022347869002260268 seconds
Training complete for VISIT with 3 states with time 0.061405729968100786 seconds
Training complete for MOVIE with 3 states with time 0.019101552024949342 seconds
Training complete for WANT with 3 states with time 0.018577218987047672 seconds
Training complete for SELL with 3 states with time 0.01831927802413702 seconds
Training complete for TOMORROW with 3 states with time 0.013570397975854576 seconds
Training complete for NEXT-WEEK with 3 states with time 0.014211617992259562 seconds
Training complete for NEW-YORK with 3 states with time 0.019246804004069418 seconds
Training complete for LAST-WEEK with 3 states with time 0.017605508968699723 seconds
Training complete for WILL with 3 states with time 0.019757245026994497 seconds
Training complete for FINISH with 3 states with time 0.03827732102945447 seconds
Training complete for ANN with 3 states with time 0.021215763001237065 seconds
Training complete for READ with 3 states with time 0.020385979034472257 seconds
Training complete for BOOK with 3 states with time 0.2689065489685163 seconds
Training complete for CHOCOLATE with 3 states with time 0.021609802963212132 seconds
Training complete for FIND with 3 states with time 0.014913927007000893 seconds
Training complete for SOMETHING-ONE with 3 states with time 0.037538231001235545 seconds
Training complete for POSS with 3 states with time 0.05708917003357783 seconds
Training complete for BROTHER with 3 states with time 0.019447893020696938 seconds
Training complete for ARRIVE with 3 states with time 0.05217659298796207 seconds
Training complete for HERE with 3 states with time 0.02331163000781089 seconds
Training complete for GIVE with 3 states with time 0.05084023700328544 seconds
Training complete for MAN with 3 states with time 0.02251850801985711 seconds
Training complete for NEW with 3 states with time 0.038907794980332255 seconds
Training complete for COAT with 3 states with time 0.018747805035673082 seconds
Training complete for WOMAN with 3 states with time 0.04493241902673617 seconds
Training complete for GIVE1 with 3 states with time 0.0862918589846231 seconds
Training complete for HAVE with 3 states with time 0.038709545973688364 seconds
Training complete for FRANK with 3 states with time 0.02155644999584183 seconds
Training complete for BREAK-DOWN with 3 states with time 0.021395289979409426 seconds
Training complete for SEARCH-FOR with 3 states with time 0.018218655022792518 seconds
Training complete for WHO with 3 states with time 0.09095929702743888 seconds
Training complete for WHAT with 3 states with time 0.09745568595826626 seconds
Training complete for LEG with 3 states with time 0.017640422040130943 seconds
Training complete for FRIEND with 3 states with time 0.016466492030303925 seconds
Training complete for CANDY with 3 states with time 0.014565767021849751 seconds
Training complete for BLUE with 3 states with time 0.019300412037409842 seconds
Training complete for SUE with 3 states with time 0.02296758204465732 seconds
Training complete for BUY1 with 3 states with time 0.037951595964841545 seconds
Training complete for STOLEN with 3 states with time 0.016517848998773843 seconds
Training complete for OLD with 3 states with time 0.013871266972273588 seconds
Training complete for STUDENT with 3 states with time 0.02080287301214412 seconds
Training complete for VIDEOTAPE with 3 states with time 0.020094520994462073 seconds
Training complete for BORROW with 3 states with time 0.01616956398356706 seconds
Training complete for MOTHER with 3 states with time 0.019120629003737122 seconds
Training complete for POTATO with 3 states with time 0.016599980008322746 seconds
Training complete for TELL with 3 states with time 0.023527454992290586 seconds
Training complete for BILL with 3 states with time 0.026364909019321203 seconds
Training complete for THROW with 3 states with time 0.023958562989719212 seconds
Training complete for APPLE with 3 states with time 0.02378294599475339 seconds
Training complete for NAME with 3 states with time 0.015308617963455617 seconds
Training complete for SHOOT with 3 states with time 0.014900978014338762 seconds
Training complete for SAY-1P with 3 states with time 0.01344723702641204 seconds
Training complete for SELF with 3 states with time 0.0160242150304839 seconds
Training complete for GROUP with 3 states with time 0.014583254000172019 seconds
Training complete for JANA with 3 states with time 0.01928220404079184 seconds
Training complete for TOY1 with 3 states with time 0.017106613027863204 seconds
Training complete for MANY with 3 states with time 0.016336591041181237 seconds
Training complete for TOY with 3 states with time 0.017570845957379788 seconds
Training complete for ALL with 3 states with time 0.02136944205267355 seconds
Training complete for BOY with 3 states with time 0.02840200299397111 seconds
Training complete for TEACHER with 3 states with time 0.031887488963548094 seconds
Training complete for GIRL with 3 states with time 0.02608089300338179 seconds
Training complete for BOX with 3 states with time 0.03707732999464497 seconds
Training complete for GIVE2 with 3 states with time 0.016873874003067613 seconds
Training complete for GIVE3 with 3 states with time 0.019082131970208138 seconds
Training complete for GET with 3 states with time 0.016045961994677782 seconds
Training complete for PUTASIDE with 3 states with time 0.01746163098141551 seconds
Number of word models returned = 112
'19/04/2017 04:36:12 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:36:12 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:36:21 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5955056179775281
Total correct: 72 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: *GO WRITE HOMEWORK                                            JOHN WRITE HOMEWORK
    7: JOHN *PEOPLE *MARY *ARRIVE                                    JOHN CAN GO CAN
   12: JOHN *HAVE *WHAT CAN                                          JOHN CAN GO CAN
   21: JOHN *VIDEOTAPE *NEW *MARY *CAR *CAR *VISIT CHICKEN           JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN LIKE *MARY *LIKE IX                                      JOHN LIKE IX IX IX
   28: JOHN LIKE *MARY *LIKE *MARY                                   JOHN LIKE IX IX IX
   30: *IX LIKE IX *MARY IX                                          JOHN LIKE IX IX IX
   36: MARY VEGETABLE *YESTERDAY *GIVE *MARY *MARY                   MARY VEGETABLE KNOW IX LIKE CORN1
   40: *MARY *MARY *CORN *VEGETABLE *IX                              JOHN IX THINK MARY LOVE
   43: *FRANK *FUTURE BUY HOUSE                                      JOHN MUST BUY HOUSE
   50: *FRANK *SEE BUY CAR *SOMETHING-ONE                            FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *FUTURE BUY HOUSE                                 JOHN SHOULD NOT BUY HOUSE
   57: *MARY *JOHN *MARY *IX                                         JOHN DECIDE VISIT MARY
   67: *LIKE FUTURE NOT BUY HOUSE                                    JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE *GO MARY                                         JOHN WILL VISIT MARY
   74: *IX *MARY *MARY *GO                                           JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *ARRIVE *HOMEWORK BOOK                                  IX-1P FIND SOMETHING-ONE BOOK
   89: *FUTURE *POSS *IX *IX IX NEW *BREAK-DOWN                      JOHN IX GIVE MAN IX NEW COAT
   90: *POSS *GIVE1 IX *IX WOMAN *CHOCOLATE                          JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *GIVE1 IX *WOMAN WOMAN BOOK                              JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: *FRANK *SEE                                                   JOHN LEG
  107: *LIKE *IX *HAVE *MARY *JANA                                   JOHN POSS FRIEND HAVE CANDY
  108: WOMAN *BOOK                                                   WOMAN ARRIVE
  113: IX CAR *IX *IX *BOX                                           IX CAR BLUE SUE BUY
  119: *PREFER *BUY1 IX CAR *IX                                      SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 *COAT                                             JOHN READ BOOK
  139: *IX *BUY1 *BOX YESTERDAY BOOK                                 JOHN BUY WHAT YESTERDAY BOOK
  142: *FRANK *NEW *CHICAGO WHAT BOOK                                JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *MARY WHO                                                LOVE JOHN WHO
  167: *MARY IX *MARY LOVE *LOVE                                     JOHN IX SAY LOVE MARY
  171: *SOMETHING-ONE *SOMETHING-ONE BLAME                           JOHN MARY BLAME
  174: *ARRIVE *GIVE3 GIVE1 *GIVE *WHAT                              PEOPLE GROUP GIVE1 JANA TOY
  181: *VISIT *BOX                                                   JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER APPLE                                  ALL BOY GIVE TEACHER APPLE
  189: *JANA *IX *GIVE BOX                                           JOHN GIVE GIRL BOX
  193: JOHN *SOMETHING-ONE *YESTERDAY BOX                            JOHN GIVE GIRL BOX
  199: *JOHN CHOCOLATE WHO                                           LIKE CHOCOLATE WHO
  201: JOHN *SHOULD *WOMAN *LOVE *BOOK HOUSE                         JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:36:21 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:36:21 PM' - root - DEBUG - Please wait...
'19/04/2017 04:36:55 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:36:55 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, right
Chosen Model Selector:  SelectorCV
Training complete for JOHN with 3 states with time 22.94752237398643 seconds
Training complete for WRITE with 10 states with time 0.25092956895241514 seconds
Training complete for HOMEWORK with 7 states with time 0.22611920296913013 seconds
Training complete for IX-1P with 2 states with time 0.7115067160339095 seconds
Training complete for SEE with 3 states with time 0.8445208680350333 seconds
Training complete for YESTERDAY with 2 states with time 1.1438431940041482 seconds
Training complete for IX with 3 states with time 7.683233980031218 seconds
Training complete for LOVE with 3 states with time 2.0367918409756385 seconds
Training complete for MARY with 6 states with time 5.845311112992931 seconds
Training complete for CAN with 5 states with time 2.1859044769662432 seconds
Training complete for GO with 4 states with time 1.4498028850066476 seconds
Training complete for GO1 with 6 states with time 0.7492448289995082 seconds
Training complete for FUTURE with 2 states with time 2.0437351490254514 seconds
Training complete for GO2 with 4 states with time 0.0782668279716745 seconds
Training complete for PARTY with 8 states with time 0.15641899994807318 seconds
Training complete for FUTURE1 with 5 states with time 0.19673389999661595 seconds
Training complete for HIT with 7 states with time 0.16126333002466708 seconds
Training complete for BLAME with 2 states with time 0.8029019319801591 seconds
Training complete for FRED with 5 states with time 0.1739982920116745 seconds
Training complete for FISH with 6 states with time 0.22641226701671258 seconds
Training complete for WONT with 2 states with time 0.3694355670013465 seconds
Training complete for EAT with 2 states with time 0.36585897795157507 seconds
Training complete for BUT with 10 states with time 0.2176884589716792 seconds
Training complete for CHICKEN with 8 states with time 0.23955491196829826 seconds
Training complete for VEGETABLE with 2 states with time 0.9900045029935427 seconds
Training complete for CHINA with 10 states with time 0.2353622670052573 seconds
Training complete for PEOPLE with 2 states with time 0.7184923370368779 seconds
Training complete for PREFER with 2 states with time 0.6478476200136356 seconds
Training complete for BROCCOLI with 7 states with time 0.25017088698223233 seconds
Training complete for LIKE with 2 states with time 1.2793439870001748 seconds
Training complete for LEAVE with 5 states with time 0.3501859839889221 seconds
Training complete for SAY with 5 states with time 0.21819161099847406 seconds
Training complete for BUY with 4 states with time 2.175980351981707 seconds
Training complete for HOUSE with 2 states with time 1.6812151920166798 seconds
Training complete for KNOW with 2 states with time 0.32237792399246246 seconds
Training complete for CORN with 2 states with time 0.5689211409771815 seconds
Training complete for CORN1 with 7 states with time 0.2607081269961782 seconds
Training complete for THINK with 5 states with time 0.2322589789982885 seconds
Training complete for NOT with 2 states with time 1.1685936910216697 seconds
Training complete for PAST with 7 states with time 0.18472152203321457 seconds
Training complete for LIVE with 4 states with time 0.07899535301839933 seconds
Training complete for CHICAGO with 7 states with time 0.1903141459915787 seconds
Training complete for CAR with 2 states with time 2.277005926007405 seconds
Training complete for SHOULD with 4 states with time 1.3101262589916587 seconds
Training complete for DECIDE with 9 states with time 0.2354170250473544 seconds
Training complete for VISIT with 2 states with time 1.5519727309583686 seconds
Training complete for MOVIE with 7 states with time 0.22104094497626647 seconds
Training complete for WANT with 8 states with time 0.22935822495492175 seconds
Training complete for SELL with 4 states with time 0.4006789569975808 seconds
Training complete for TOMORROW with 6 states with time 0.20192826498532668 seconds
Training complete for NEXT-WEEK with 5 states with time 0.10413610795512795 seconds
Training complete for NEW-YORK with 8 states with time 0.2151170169818215 seconds
Training complete for LAST-WEEK with 10 states with time 0.19654040603199974 seconds
Training complete for WILL with 5 states with time 0.2044867139775306 seconds
Training complete for FINISH with 2 states with time 0.7923137710313313 seconds
Training complete for ANN with 6 states with time 0.2301494479761459 seconds
Training complete for READ with 2 states with time 0.6323868589824997 seconds
Training complete for BOOK with 2 states with time 2.043112860992551 seconds
Training complete for CHOCOLATE with 2 states with time 0.569140135019552 seconds
Training complete for FIND with 2 states with time 0.04468685801839456 seconds
Training complete for SOMETHING-ONE with 4 states with time 1.4771128660067916 seconds
Training complete for POSS with 2 states with time 1.1293089400278404 seconds
Training complete for BROTHER with 10 states with time 0.25664808700094 seconds
Training complete for ARRIVE with 2 states with time 1.8523226560209878 seconds
Training complete for HERE with 2 states with time 0.317396174010355 seconds
Training complete for GIVE with 2 states with time 1.403109002043493 seconds
Training complete for MAN with 10 states with time 0.2559366619680077 seconds
Training complete for NEW with 5 states with time 0.7670921200187877 seconds
Training complete for COAT with 10 states with time 0.24121254298370332 seconds
Training complete for WOMAN with 2 states with time 1.2505300450138748 seconds
Training complete for GIVE1 with 2 states with time 1.2928587270434946 seconds
Training complete for HAVE with 2 states with time 0.8544644010253251 seconds
Training complete for FRANK with 2 states with time 0.724944943038281 seconds
Training complete for BREAK-DOWN with 2 states with time 0.6797632439993322 seconds
Training complete for SEARCH-FOR with 8 states with time 0.22662277199560776 seconds
Training complete for WHO with 4 states with time 2.1964617429766804 seconds
Training complete for WHAT with 2 states with time 3.2313819749979302 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 0.1868908730102703 seconds
Training complete for CANDY with 2 states with time 0.1839023240027018 seconds
Training complete for BLUE with 2 states with time 0.2816602989914827 seconds
Training complete for SUE with 2 states with time 0.5249424990033731 seconds
Training complete for BUY1 with 7 states with time 0.8710322779952548 seconds
Training complete for STOLEN with 10 states with time 0.26134388498030603 seconds
Training complete for OLD with 2 states with time 0.15836790297180414 seconds
Training complete for STUDENT with 2 states with time 0.44024323095800355 seconds
Training complete for VIDEOTAPE with 2 states with time 0.5591937690041959 seconds
Training complete for BORROW with 3 states with time 0.08332838700152934 seconds
Training complete for MOTHER with 2 states with time 0.4698590339976363 seconds
Training complete for POTATO with 7 states with time 0.19649275997653604 seconds
Training complete for TELL with 2 states with time 0.8134140130132437 seconds
Training complete for BILL with 2 states with time 0.8295463579706848 seconds
Training complete for THROW with 4 states with time 0.7627159359981306 seconds
Training complete for APPLE with 2 states with time 0.7900695989956148 seconds
Training complete for NAME with 10 states with time 0.18955117103178054 seconds
Training complete for SHOOT with 10 states with time 0.20515076600713655 seconds
Training failed for SAY-1P
Training complete for SELF with 10 states with time 0.20635189901804551 seconds
Training complete for GROUP with 7 states with time 0.15135298698442057 seconds
Training complete for JANA with 10 states with time 0.22756040300009772 seconds
Training complete for TOY1 with 8 states with time 0.18781947501702234 seconds
Training complete for MANY with 3 states with time 0.1548685469897464 seconds
Training complete for TOY with 4 states with time 0.224466972053051 seconds
Training complete for ALL with 8 states with time 0.22508897195803002 seconds
Training complete for BOY with 4 states with time 0.3987379539757967 seconds
Training complete for TEACHER with 3 states with time 0.7554446079884656 seconds
Training complete for GIRL with 2 states with time 0.6107433429569937 seconds
Training complete for BOX with 2 states with time 0.9724291830207221 seconds
Training complete for GIVE2 with 7 states with time 0.21720358496531844 seconds
Training complete for GIVE3 with 10 states with time 0.2540300670079887 seconds
Training complete for GET with 7 states with time 0.12453233398264274 seconds
Training complete for PUTASIDE with 5 states with time 0.1987499640090391 seconds
Number of word models returned = 112
'19/04/2017 04:38:49 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:38:49 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:38:59 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5617977528089888
Total correct: 78 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN WRITE *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN *PEOPLE GO CAN                                           JOHN CAN GO CAN
   12: JOHN CAN *WHAT CAN                                            JOHN CAN GO CAN
   21: JOHN *NEW *NEW *MARY *CAR *CAR *VISIT *GO                     JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN LIKE IX *LIKE IX                                         JOHN LIKE IX IX IX
   28: JOHN *MARY IX *LIKE IX                                        JOHN LIKE IX IX IX
   30: *IX LIKE IX IX IX                                             JOHN LIKE IX IX IX
   36: MARY *MARY *YESTERDAY *GIVE *IX *JOHN                         MARY VEGETABLE KNOW IX LIKE CORN1
   40: JOHN IX *CORN MARY *IX                                        JOHN IX THINK MARY LOVE
   43: *FRANK *SHOULD BUY HOUSE                                      JOHN MUST BUY HOUSE
   50: *FRANK *SEE BUY CAR SHOULD                                    FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD *MARY BUY HOUSE                                   JOHN SHOULD NOT BUY HOUSE
   57: *IX *GO VISIT *IX                                             JOHN DECIDE VISIT MARY
   67: JOHN *POSS NOT *ARRIVE HOUSE                                  JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FINISH *BLAME MARY                                      JOHN WILL VISIT MARY
   74: *IX *VISIT *MARY MARY                                         JOHN NOT VISIT MARY
   77: *IX BLAME *IX                                                 ANN BLAME MARY
   84: *JOHN *ARRIVE *BLAME BOOK                                     IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *SOMETHING-ONE *IX *IX IX NEW *BREAK-DOWN               JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *GIVE1 *SOMETHING-ONE *GIVE1 WOMAN *VIDEOTAPE            JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *WOMAN *WOMAN *WOMAN *IX BOOK                            JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: *FRANK NEW CAR BREAK-DOWN                                     POSS NEW CAR BREAK-DOWN
  105: *FRANK *FRANK                                                 JOHN LEG
  107: *LIKE *GO *HAVE *MARY *MARY                                   JOHN POSS FRIEND HAVE CANDY
  108: *MARY *BOOK                                                   WOMAN ARRIVE
  113: IX CAR *SUE SUE *BOX                                          IX CAR BLUE SUE BUY
  119: *PREFER *BUY1 *GO *WHAT *GO                                   SUE BUY IX CAR BLUE
  122: JOHN *HOUSE BOOK                                              JOHN READ BOOK
  139: JOHN *BOOK *PEOPLE YESTERDAY *GIVE1                           JOHN BUY WHAT YESTERDAY BOOK
  142: *FRANK *NEW YESTERDAY WHAT BOOK                               JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE *MARY WHO                                                LOVE JOHN WHO
  167: JOHN *SUE *VISIT *IX MARY                                     JOHN IX SAY LOVE MARY
  171: JOHN *SUE BLAME                                               JOHN MARY BLAME
  174: *GIVE1 *GIVE1 GIVE1 *GIRL *WHAT                               PEOPLE GROUP GIVE1 JANA TOY
  181: *VISIT *BOX                                                   JOHN ARRIVE
  184: *GIVE1 BOY *GIVE1 TEACHER APPLE                               ALL BOY GIVE TEACHER APPLE
  189: JOHN *VISIT *CORN BOX                                         JOHN GIVE GIRL BOX
  193: JOHN *SOMETHING-ONE *YESTERDAY BOX                            JOHN GIVE GIRL BOX
  199: *JOHN CHOCOLATE *TELL                                         LIKE CHOCOLATE WHO
  201: JOHN *MARY *WOMAN *LOVE *ARRIVE HOUSE                         JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:38:59 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:38:59 PM' - root - DEBUG - Please wait...
'19/04/2017 04:39:33 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:39:33 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, right
Chosen Model Selector:  SelectorBIC
Training complete for JOHN with 10 states with time 12.842248277971521 seconds
Training complete for WRITE with 10 states with time 0.2687522579799406 seconds
Training complete for HOMEWORK with 7 states with time 0.2868129350244999 seconds
Training complete for IX-1P with 10 states with time 0.3978140489780344 seconds
Training complete for SEE with 10 states with time 0.5050421609776095 seconds
Training complete for YESTERDAY with 10 states with time 0.5399723589653149 seconds
Training complete for IX with 10 states with time 5.671836211986374 seconds
Training complete for LOVE with 10 states with time 1.1658117159968242 seconds
Training complete for MARY with 10 states with time 3.371728982019704 seconds
Training complete for CAN with 10 states with time 1.2359826730098575 seconds
Training complete for GO with 10 states with time 0.853462835017126 seconds
Training complete for GO1 with 10 states with time 0.3306040579918772 seconds
Training complete for FUTURE with 10 states with time 1.0747619660105556 seconds
Training complete for GO2 with 4 states with time 0.08645574399270117 seconds
Training complete for PARTY with 8 states with time 0.17096111201681197 seconds
Training complete for FUTURE1 with 5 states with time 0.2571588569553569 seconds
Training complete for HIT with 7 states with time 0.1596365129807964 seconds
Training complete for BLAME with 10 states with time 0.34945749799953774 seconds
Training complete for FRED with 5 states with time 0.16007252101553604 seconds
Training complete for FISH with 6 states with time 0.22981423296732828 seconds
Training complete for WONT with 7 states with time 0.26327226200373843 seconds
Training complete for EAT with 6 states with time 0.2847673619980924 seconds
Training complete for BUT with 10 states with time 0.23948273598216474 seconds
Training complete for CHICKEN with 8 states with time 0.24539002799429 seconds
Training complete for VEGETABLE with 10 states with time 0.4311779520357959 seconds
Training complete for CHINA with 10 states with time 0.2520108410390094 seconds
Training complete for PEOPLE with 10 states with time 0.41500940098194405 seconds
Training complete for PREFER with 9 states with time 0.49153834203025326 seconds
Training complete for BROCCOLI with 7 states with time 0.29159719799645245 seconds
Training complete for LIKE with 10 states with time 0.547352112014778 seconds
Training complete for LEAVE with 10 states with time 0.24290232197381556 seconds
Training complete for SAY with 5 states with time 0.2725500400410965 seconds
Training complete for BUY with 10 states with time 1.1493461669888347 seconds
Training complete for HOUSE with 10 states with time 0.798813647008501 seconds
Training complete for KNOW with 3 states with time 0.2427051619742997 seconds
Training complete for CORN with 10 states with time 0.35394828801508993 seconds
Training complete for CORN1 with 6 states with time 0.26390217198058963 seconds
Training complete for THINK with 5 states with time 0.2406449969857931 seconds
Training complete for NOT with 10 states with time 0.6135940430103801 seconds
Training complete for PAST with 7 states with time 0.19756808399688452 seconds
Training complete for LIVE with 4 states with time 0.07982728898059577 seconds
Training complete for CHICAGO with 7 states with time 0.18689375196117908 seconds
Training complete for CAR with 10 states with time 1.2392956389812753 seconds
Training complete for SHOULD with 10 states with time 0.6499378880253062 seconds
Training complete for DECIDE with 9 states with time 0.23924577003344893 seconds
Training complete for VISIT with 10 states with time 0.6938626000192016 seconds
Training complete for MOVIE with 7 states with time 0.23007632402004674 seconds
Training complete for WANT with 8 states with time 0.2304202990490012 seconds
Training complete for SELL with 10 states with time 0.24474547401769087 seconds
Training complete for TOMORROW with 6 states with time 0.19924998900387436 seconds
Training complete for NEXT-WEEK with 5 states with time 0.10909606900531799 seconds
Training complete for NEW-YORK with 8 states with time 0.22713321802439168 seconds
Training complete for LAST-WEEK with 10 states with time 0.20597608399111778 seconds
Training complete for WILL with 5 states with time 0.21947832801379263 seconds
Training complete for FINISH with 10 states with time 0.3308892600471154 seconds
Training complete for ANN with 6 states with time 0.20561408501816913 seconds
Training complete for READ with 10 states with time 0.26232661202084273 seconds
Training complete for BOOK with 10 states with time 1.3537117670057341 seconds
Training complete for CHOCOLATE with 10 states with time 0.26877940294798464 seconds
Training complete for FIND with 2 states with time 0.045101593947038054 seconds
Training complete for SOMETHING-ONE with 10 states with time 0.5960443989606574 seconds
Training complete for POSS with 10 states with time 0.6122666859882884 seconds
Training complete for BROTHER with 9 states with time 0.23790411301888525 seconds
Training complete for ARRIVE with 10 states with time 1.0536662429803982 seconds
Training complete for HERE with 9 states with time 0.269984781043604 seconds
Training complete for GIVE with 10 states with time 0.6262202319921926 seconds
Training complete for MAN with 10 states with time 0.26407219003885984 seconds
Training complete for NEW with 10 states with time 0.4481303070206195 seconds
Training complete for COAT with 10 states with time 0.24326589202973992 seconds
Training complete for WOMAN with 10 states with time 0.5705338129773736 seconds
Training complete for GIVE1 with 10 states with time 0.6993571469793096 seconds
Training complete for HAVE with 10 states with time 0.35170269198715687 seconds
Training complete for FRANK with 10 states with time 0.3078662859625183 seconds
Training complete for BREAK-DOWN with 6 states with time 0.3817915709805675 seconds
Training complete for SEARCH-FOR with 8 states with time 0.22826131799956784 seconds
Training complete for WHO with 10 states with time 1.5118017250206321 seconds
Training complete for WHAT with 10 states with time 1.891096830018796 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 0.20399581600213423 seconds
Training complete for CANDY with 2 states with time 0.18909047194756567 seconds
Training complete for BLUE with 6 states with time 0.2821714059682563 seconds
Training complete for SUE with 10 states with time 0.30003699799999595 seconds
Training complete for BUY1 with 10 states with time 0.49350057198898867 seconds
Training complete for STOLEN with 10 states with time 0.29921369801741093 seconds
Training complete for OLD with 2 states with time 0.16676008998183534 seconds
Training complete for STUDENT with 10 states with time 0.2780341129982844 seconds
Training complete for VIDEOTAPE with 10 states with time 0.30313467496307567 seconds
Training complete for BORROW with 3 states with time 0.08714613504707813 seconds
Training complete for MOTHER with 10 states with time 0.24969779298407957 seconds
Training complete for POTATO with 7 states with time 0.20140156999696046 seconds
Training complete for TELL with 10 states with time 0.3128202660009265 seconds
Training complete for BILL with 10 states with time 0.39155353599926457 seconds
Training complete for THROW with 9 states with time 0.27271844597999007 seconds
Training complete for APPLE with 10 states with time 0.3353197129908949 seconds
Training complete for NAME with 5 states with time 0.20358564803609625 seconds
Training complete for SHOOT with 10 states with time 0.21505129901925102 seconds
Training failed for SAY-1P
Training complete for SELF with 8 states with time 0.2093975770403631 seconds
Training complete for GROUP with 7 states with time 0.1577638169983402 seconds
Training complete for JANA with 10 states with time 0.24361163598950952 seconds
Training complete for TOY1 with 8 states with time 0.1946062150527723 seconds
Training complete for MANY with 3 states with time 0.1600026660016738 seconds
Training complete for TOY with 4 states with time 0.2176547339768149 seconds
Training complete for ALL with 8 states with time 0.23796280502574518 seconds
Training complete for BOY with 8 states with time 0.31849436002084985 seconds
Training complete for TEACHER with 10 states with time 0.3769079650519416 seconds
Training complete for GIRL with 9 states with time 0.355927629978396 seconds
Training complete for BOX with 10 states with time 0.49550314602674916 seconds
Training complete for GIVE2 with 7 states with time 0.20770600502146408 seconds
Training complete for GIVE3 with 10 states with time 0.2847673309734091 seconds
Training complete for GET with 7 states with time 0.1430163840414025 seconds
Training complete for PUTASIDE with 5 states with time 0.265035321994219 seconds
Number of word models returned = 112
'19/04/2017 04:40:46 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:40:46 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:40:57 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.48314606741573035
Total correct: 92 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN WRITE *JOHN                                              JOHN WRITE HOMEWORK
    7: JOHN *VISIT GO CAN                                            JOHN CAN GO CAN
   12: *IX *WHAT *CAN *WHAT                                          JOHN CAN GO CAN
   21: JOHN *NEW *JOHN *MARY *JOHN *WHAT *FUTURE *FUTURE             JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *IX *LOVE IX IX                                          JOHN LIKE IX IX IX
   28: JOHN *MARY IX IX IX                                           JOHN LIKE IX IX IX
   30: JOHN *MARY IX *MARY IX                                        JOHN LIKE IX IX IX
   36: MARY *VISIT *GIVE IX *MARY *MARY                              MARY VEGETABLE KNOW IX LIKE CORN1
   40: *MARY IX *GIVE MARY *IX                                       JOHN IX THINK MARY LOVE
   43: JOHN *JOHN BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *JOHN JOHN BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD NOT BUY HOUSE                                     JOHN SHOULD NOT BUY HOUSE
   57: *IX *MARY VISIT *IX                                           JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *MARY BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE VISIT MARY                                       JOHN WILL VISIT MARY
   74: *IX *VISIT VISIT MARY                                         JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *ARRIVE *VISIT BOOK                                     IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *POSS *IX *IX IX NEW *BREAK-DOWN                        JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX WOMAN BOOK                                    JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *WOMAN IX *IX WOMAN BOOK                                 JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *FRANK                                                   JOHN LEG
  107: JOHN *IX *JOHN *MARY *JOHN                                    JOHN POSS FRIEND HAVE CANDY
  108: *IX *HOMEWORK                                                 WOMAN ARRIVE
  113: IX CAR *IX *IX *BOX                                           IX CAR BLUE SUE BUY
  119: *MARY *BUY1 IX *BLAME *JOHN                                   SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: JOHN *BUY1 WHAT *JOHN BOOK                                    JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *VISIT LOVE MARY                                      JOHN IX SAY LOVE MARY
  171: JOHN *JOHN BLAME                                              JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *GIVE *JOHN                                PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER *GIVE                                  ALL BOY GIVE TEACHER APPLE
  189: *MARY *GO *GIVE BOX                                           JOHN GIVE GIRL BOX
  193: JOHN *IX *GIVE BOX                                            JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *MARY *WOMAN *JOHN BUY HOUSE                             JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:40:57 PM' - root - DEBUG - Loading training data sequences from CSV file suitable for HMMlearn lib based on feature method chosen.
'19/04/2017 04:40:57 PM' - root - DEBUG - Please wait...
'19/04/2017 04:41:30 PM' - root - DEBUG - Loaded into consolidated sequenced (samples) feature data into a dictionary of words from CSV file containing word training data...
'19/04/2017 04:41:30 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Available Training words - words:  ['JOHN', 'WRITE', 'HOMEWORK', 'IX-1P', 'SEE', 'YESTERDAY', 'IX', 'LOVE', 'MARY', 'CAN', 'GO', 'GO1', 'FUTURE', 'GO2', 'PARTY', 'FUTURE1', 'HIT', 'BLAME', 'FRED', 'FISH', 'WONT', 'EAT', 'BUT', 'CHICKEN', 'VEGETABLE', 'CHINA', 'PEOPLE', 'PREFER', 'BROCCOLI', 'LIKE', 'LEAVE', 'SAY', 'BUY', 'HOUSE', 'KNOW', 'CORN', 'CORN1', 'THINK', 'NOT', 'PAST', 'LIVE', 'CHICAGO', 'CAR', 'SHOULD', 'DECIDE', 'VISIT', 'MOVIE', 'WANT', 'SELL', 'TOMORROW', 'NEXT-WEEK', 'NEW-YORK', 'LAST-WEEK', 'WILL', 'FINISH', 'ANN', 'READ', 'BOOK', 'CHOCOLATE', 'FIND', 'SOMETHING-ONE', 'POSS', 'BROTHER', 'ARRIVE', 'HERE', 'GIVE', 'MAN', 'NEW', 'COAT', 'WOMAN', 'GIVE1', 'HAVE', 'FRANK', 'BREAK-DOWN', 'SEARCH-FOR', 'WHO', 'WHAT', 'LEG', 'FRIEND', 'CANDY', 'BLUE', 'SUE', 'BUY1', 'STOLEN', 'OLD', 'STUDENT', 'VIDEOTAPE', 'BORROW', 'MOTHER', 'POTATO', 'TELL', 'BILL', 'THROW', 'APPLE', 'NAME', 'SHOOT', 'SAY-1P', 'SELF', 'GROUP', 'JANA', 'TOY1', 'MANY', 'TOY', 'ALL', 'BOY', 'TEACHER', 'GIRL', 'BOX', 'GIVE2', 'GIVE3', 'GET', 'PUTASIDE']
Quantity of Training words - num_items:  112
CV Chosen Training words: All words
Chosen Features:  grnd, norm, polar, right
Chosen Model Selector:  SelectorDIC
Training complete for JOHN with 10 states with time 14.025227255013306 seconds
Training complete for WRITE with 10 states with time 2.0661156509886496 seconds
Training complete for HOMEWORK with 5 states with time 0.8031822280026972 seconds
Training complete for IX-1P with 8 states with time 2.223998287052382 seconds
Training complete for SEE with 10 states with time 2.261522138956934 seconds
Training complete for YESTERDAY with 10 states with time 2.367620470991824 seconds
Training complete for IX with 10 states with time 6.966960382007528 seconds
Training complete for LOVE with 10 states with time 2.7759854779578745 seconds
Training complete for MARY with 10 states with time 4.952345645986497 seconds
Training complete for CAN with 10 states with time 2.873662134981714 seconds
Training complete for GO with 10 states with time 2.5859334699925967 seconds
Training complete for GO1 with 10 states with time 2.1026901709847152 seconds
Training complete for FUTURE with 10 states with time 2.8513403249671683 seconds
Training complete for GO2 with 4 states with time 0.6477453599800356 seconds
Training complete for PARTY with 8 states with time 1.8460971669992432 seconds
Training complete for FUTURE1 with 5 states with time 0.9499596569803543 seconds
Training complete for HIT with 7 states with time 1.3836466110078618 seconds
Training complete for BLAME with 10 states with time 2.23456554999575 seconds
Training complete for FRED with 5 states with time 0.9873319199541584 seconds
Training complete for FISH with 6 states with time 1.176551294978708 seconds
Training complete for WONT with 7 states with time 1.2979763220064342 seconds
Training complete for EAT with 6 states with time 1.0520325689576566 seconds
Training complete for BUT with 10 states with time 2.1656603519804776 seconds
Training complete for CHICKEN with 8 states with time 1.5492159569985233 seconds
Training complete for VEGETABLE with 10 states with time 2.2383566650096327 seconds
Training complete for CHINA with 10 states with time 2.1552401789813302 seconds
Training complete for PEOPLE with 10 states with time 2.0562430690042675 seconds
Training complete for PREFER with 10 states with time 2.1681598279974423 seconds
Training complete for BROCCOLI with 5 states with time 1.3024087229860015 seconds
Training complete for LIKE with 10 states with time 2.26211950101424 seconds
Training complete for LEAVE with 4 states with time 2.1528304319945164 seconds
Training complete for SAY with 2 states with time 0.8094141710316762 seconds
Training complete for BUY with 10 states with time 2.7854821319924667 seconds
Training complete for HOUSE with 10 states with time 2.4503938870038837 seconds
Training complete for KNOW with 3 states with time 0.37939426803495735 seconds
Training complete for CORN with 10 states with time 2.192880218033679 seconds
Training complete for CORN1 with 2 states with time 1.3103597339941189 seconds
Training complete for THINK with 3 states with time 0.8119987070094794 seconds
Training complete for NOT with 10 states with time 2.3229613750008866 seconds
Training complete for PAST with 2 states with time 1.227828186005354 seconds
Training complete for LIVE with 4 states with time 0.5872424480039626 seconds
Training complete for CHICAGO with 7 states with time 1.2833681489573792 seconds
Training complete for CAR with 9 states with time 2.7942381750326604 seconds
Training complete for SHOULD with 10 states with time 2.412535793031566 seconds
Training complete for DECIDE with 9 states with time 1.9418858689605258 seconds
Training complete for VISIT with 9 states with time 2.3266677240026183 seconds
Training complete for MOVIE with 7 states with time 1.3192604079958983 seconds
Training complete for WANT with 8 states with time 1.5422913869842887 seconds
Training complete for SELL with 10 states with time 2.1288970679743215 seconds
Training complete for TOMORROW with 6 states with time 1.062181416025851 seconds
Training complete for NEXT-WEEK with 5 states with time 0.8145512280170806 seconds
Training complete for NEW-YORK with 8 states with time 1.6626828989828937 seconds
Training complete for LAST-WEEK with 10 states with time 2.211507725995034 seconds
Training complete for WILL with 5 states with time 0.7939611399779096 seconds
Training complete for FINISH with 10 states with time 2.0850692550302483 seconds
Training complete for ANN with 2 states with time 1.0888699209899642 seconds
Training complete for READ with 9 states with time 2.633606461051386 seconds
Training complete for BOOK with 10 states with time 3.374174166994635 seconds
Training complete for CHOCOLATE with 10 states with time 2.072257542051375 seconds
Training complete for FIND with 2 states with time 0.19412057200679556 seconds
Training complete for SOMETHING-ONE with 10 states with time 2.5545752230100334 seconds
Training complete for POSS with 10 states with time 2.8034730320214294 seconds
Training complete for BROTHER with 10 states with time 2.1288602349814028 seconds
Training complete for ARRIVE with 9 states with time 2.796566509990953 seconds
Training complete for HERE with 6 states with time 1.9048757380223833 seconds
Training complete for GIVE with 2 states with time 2.7725444809766486 seconds
Training complete for MAN with 10 states with time 2.4718132590060122 seconds
Training complete for NEW with 9 states with time 2.658330978010781 seconds
Training complete for COAT with 10 states with time 2.2611919920309447 seconds
Training complete for WOMAN with 10 states with time 2.2814390280400403 seconds
Training complete for GIVE1 with 10 states with time 2.552585875033401 seconds
Training complete for HAVE with 10 states with time 2.5585982669726945 seconds
Training complete for FRANK with 7 states with time 2.349043759983033 seconds
Training complete for BREAK-DOWN with 6 states with time 1.1266176569624804 seconds
Training complete for SEARCH-FOR with 8 states with time 1.6096745660179295 seconds
Training complete for WHO with 10 states with time 3.2015232959529385 seconds
Training complete for WHAT with 10 states with time 3.4361065169796348 seconds
Training failed for LEG
Training complete for FRIEND with 6 states with time 1.0251410680357367 seconds
Training complete for CANDY with 2 states with time 0.2089397159870714 seconds
Training complete for BLUE with 6 states with time 1.0406424840330146 seconds
Training complete for SUE with 10 states with time 2.201112064998597 seconds
Training complete for BUY1 with 8 states with time 2.1286282939836383 seconds
Training complete for STOLEN with 10 states with time 2.160985578026157 seconds
Training complete for OLD with 2 states with time 0.18429932097205892 seconds
Training complete for STUDENT with 10 states with time 1.944313287967816 seconds
Training complete for VIDEOTAPE with 10 states with time 2.2243012560065836 seconds
Training complete for BORROW with 3 states with time 0.4198375020059757 seconds
Training complete for MOTHER with 10 states with time 2.2441069509950466 seconds
Training complete for POTATO with 7 states with time 1.3855661369743757 seconds
Training complete for TELL with 10 states with time 2.693898227997124 seconds
Training complete for BILL with 9 states with time 2.379760568961501 seconds
Training complete for THROW with 2 states with time 2.024846114043612 seconds
Training complete for APPLE with 10 states with time 2.275910786993336 seconds
Training complete for NAME with 4 states with time 2.3868129780166782 seconds
Training complete for SHOOT with 10 states with time 2.070023381966166 seconds
Training failed for SAY-1P
Training complete for SELF with 8 states with time 2.103843010030687 seconds
Training complete for GROUP with 7 states with time 1.556818070996087 seconds
Training complete for JANA with 10 states with time 2.144660576013848 seconds
Training complete for TOY1 with 8 states with time 1.540690777997952 seconds
Training complete for MANY with 3 states with time 0.3772686399752274 seconds
Training complete for TOY with 4 states with time 0.5675581030081958 seconds
Training complete for ALL with 7 states with time 1.6138204020098783 seconds
Training complete for BOY with 8 states with time 1.689827606023755 seconds
Training complete for TEACHER with 8 states with time 2.1520917100133374 seconds
Training complete for GIRL with 9 states with time 1.9376953020109795 seconds
Training complete for BOX with 10 states with time 2.2705433029914275 seconds
Training complete for GIVE2 with 2 states with time 1.3847848189761862 seconds
Training complete for GIVE3 with 8 states with time 2.359856905997731 seconds
Training complete for GET with 7 states with time 1.3159188579884358 seconds
Training complete for PUTASIDE with 5 states with time 0.7967177219688892 seconds
Number of word models returned = 112
'19/04/2017 04:45:22 PM' - root - DEBUG - Created HMMlearn concatenated sequence of tuples and lengths.
Number of test set items: 178
Number of test set sentences: 40
'19/04/2017 04:45:22 PM' - root - DEBUG - My Recognizer Started...
'19/04/2017 04:45:33 PM' - root - DEBUG - Showing Errors Started...
**** WER = 0.5112359550561798
Total correct: 87 out of 178
Video  Recognized                                                    Correct
=====================================================================================================
    2: JOHN WRITE *ARRIVE                                            JOHN WRITE HOMEWORK
    7: JOHN *VISIT GO CAN                                            JOHN CAN GO CAN
   12: *IX *WHAT *CAN *WHAT                                          JOHN CAN GO CAN
   21: JOHN *NEW *JOHN *MARY *CAR *CAR *FUTURE *FUTURE               JOHN FISH WONT EAT BUT CAN EAT CHICKEN
   25: JOHN *IX *LOVE IX IX                                          JOHN LIKE IX IX IX
   28: JOHN *MARY IX IX IX                                           JOHN LIKE IX IX IX
   30: JOHN *MARY IX *MARY IX                                        JOHN LIKE IX IX IX
   36: MARY *VISIT *GO *GIVE *MARY *MARY                             MARY VEGETABLE KNOW IX LIKE CORN1
   40: *MARY *GIVE *GO MARY *IX                                      JOHN IX THINK MARY LOVE
   43: JOHN *JOHN BUY HOUSE                                          JOHN MUST BUY HOUSE
   50: *JOHN JOHN BUY CAR *JOHN                                      FUTURE JOHN BUY CAR SHOULD
   54: JOHN SHOULD NOT BUY HOUSE                                     JOHN SHOULD NOT BUY HOUSE
   57: *IX *MARY VISIT *IX                                           JOHN DECIDE VISIT MARY
   67: JOHN FUTURE *MARY BUY HOUSE                                   JOHN FUTURE NOT BUY HOUSE
   71: JOHN *FUTURE *MARY MARY                                       JOHN WILL VISIT MARY
   74: *IX *VISIT *GIVE MARY                                         JOHN NOT VISIT MARY
   77: *JOHN BLAME MARY                                              ANN BLAME MARY
   84: *JOHN *JOHN *VISIT BOOK                                       IX-1P FIND SOMETHING-ONE BOOK
   89: *MARY *POSS *IX *IX IX *ARRIVE *BREAK-DOWN                    JOHN IX GIVE MAN IX NEW COAT
   90: JOHN *IX IX *IX WOMAN BOOK                                    JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
   92: JOHN *WOMAN IX *IX WOMAN BOOK                                 JOHN GIVE IX SOMETHING-ONE WOMAN BOOK
  100: POSS NEW CAR BREAK-DOWN                                       POSS NEW CAR BREAK-DOWN
  105: JOHN *FRANK                                                   JOHN LEG
  107: JOHN *IX *JOHN *MARY *JOHN                                    JOHN POSS FRIEND HAVE CANDY
  108: *IX *LOVE                                                     WOMAN ARRIVE
  113: IX CAR *IX *IX *BOX                                           IX CAR BLUE SUE BUY
  119: *MARY *BUY1 IX *BLAME *JOHN                                   SUE BUY IX CAR BLUE
  122: JOHN *GIVE1 BOOK                                              JOHN READ BOOK
  139: JOHN *BUY1 WHAT *JOHN BOOK                                    JOHN BUY WHAT YESTERDAY BOOK
  142: JOHN BUY YESTERDAY WHAT BOOK                                  JOHN BUY YESTERDAY WHAT BOOK
  158: LOVE JOHN WHO                                                 LOVE JOHN WHO
  167: JOHN IX *VISIT LOVE MARY                                      JOHN IX SAY LOVE MARY
  171: JOHN *JOHN BLAME                                              JOHN MARY BLAME
  174: *JOHN *GIVE1 GIVE1 *GO *JOHN                                  PEOPLE GROUP GIVE1 JANA TOY
  181: JOHN *BOX                                                     JOHN ARRIVE
  184: *IX BOY *GIVE1 TEACHER *GO                                    ALL BOY GIVE TEACHER APPLE
  189: *MARY *GO *VISIT BOX                                          JOHN GIVE GIRL BOX
  193: JOHN *IX *VISIT BOX                                           JOHN GIVE GIRL BOX
  199: *JOHN *ARRIVE *MARY                                           LIKE CHOCOLATE WHO
  201: JOHN *MARY *WOMAN *JOHN BUY HOUSE                             JOHN TELL MARY IX-1P BUY HOUSE
Finished processing combo... Trying others if any exist.
'19/04/2017 04:45:33 PM' - root - INFO - Finished Recogniser
