import logging
import numpy as np
import pandas as pd
from asl_data import AslDb
import timeit

def add_features_ground(asl):
    # Add df columns for 'grnd-rx', 'grnd-ly', 'grnd-lx' representing
    # differences between hand and nose locations
    asl.df['grnd-ry'] = asl.df['right-y'] - asl.df['nose-y']
    asl.df['grnd-rx'] = asl.df['right-x'] - asl.df['nose-x']
    asl.df['grnd-ly'] = asl.df['left-y'] - asl.df['nose-y']
    asl.df['grnd-lx'] = asl.df['left-x'] - asl.df['nose-x']
    return asl

def add_features_norm(asl, features_norm):
    # Copied from Jupyter Notebook for debugging

    # Standard Score equation to normalise Cartesian coordinates x and y
    def standard_score(x, m, std):
        return (x - m) / std

    df_means = asl.df.groupby('speaker', 0, None, True, True, True, False).mean()
    df_std = asl.df.groupby('speaker', 0, None, True, True, True, False).std()
    features_r_l = ['right-x', 'right-y', 'left-x', 'left-y']

    for f_index, f_val in enumerate(features_norm):
        f_mean = asl.df['speaker'].map(df_means[features_r_l[f_index]], na_action=None)
        f_std  = asl.df['speaker'].map(df_std[features_r_l[f_index]], na_action=None)
        asl.df[f_val] = standard_score(asl.df[features_r_l[f_index]], f_mean, f_std)

def add_features_polar(asl, features_ground, features_polar):
    # Copied from Jupyter Notebook for debugging

    # Convert Cartesian coordinates x and y to radius (Euclidean Norm) in Polar Coordinates
    def radius(x, y):
        return np.sqrt(x**2 + y**2)

    # Convert Cartesian coordinates x and y to angle (theta) in Polar Coordinates
    def angle(x, y):
        # Swap the x and y axes in the calculation
        # (i.e. instead of `np.arctan2(y, x)`)
        return np.arctan2(x, y)

    # Differences between hand and nose locations (see previous task where calculated)

    for f_index, f_val in enumerate(features_polar):
        if f_index % 2 == 0: # even indexes (i.e. 0, 2)
            asl.df[f_val] = radius(asl.df[features_ground[f_index]],
                                   asl.df[features_ground[f_index + 1]])
        else: # odd indexes
            asl.df[f_val] = angle(asl.df[features_ground[f_index - 1]],
                                  asl.df[features_ground[f_index]])

def add_features_delta(asl, features_delta):
    # Copied from Jupyter Notebook for debugging

    # Replace any NaN values with 0 after taking the results of the difference
    def frame_difference(f):
        return f.diff().fillna(0, None, 0, False, None, None)

    features_r_l = ['right-x', 'right-y', 'left-x', 'left-y']

    # Features representing the difference in values between one frame and the next frames

    for f_index, f_val in enumerate(features_delta):
        asl.df[f_val] = frame_difference(asl.df[features_r_l[f_index]])

def add_features_rescaling(asl, features_ground, features_rescaled):
    def rescale(orig, min, max):
        return (orig - min) / (max - min)

    df_max = asl.df.groupby('speaker').max()
    df_min = asl.df.groupby('speaker').min()

    # Differences between hand and nose locations (see previous task where calculated)
    features_ground = ['grnd-rx', 'grnd-ry', 'grnd-lx', 'grnd-ly']

    # Features representing the Max and Min
    features_max = ['right-x-max', 'right-y-max', 'left-x-max', 'left-y-max']
    features_min = ['right-x-min', 'right-y-min', 'left-x-min', 'left-y-min']

    for f_index, f_val in enumerate(features_ground):

        # Map the Max and Min onto the data
        asl.df[features_max[f_index]] = asl.df['speaker'].map(df_max[f_val], na_action=None)
        asl.df[features_min[f_index]] = asl.df['speaker'].map(df_min[f_val], na_action=None)

        # Normalise by rescaling using the Feature Scaling equation
        asl.df[features_rescaled[f_index]] = rescale(asl.df[f_val],
                                                     asl.df[features_min[f_index]],
                                                     asl.df[features_max[f_index]])

def initialise_asl_db(features):
    asl = AslDb()
    add_features_ground(asl)
    add_features_norm(asl, features[1])
    add_features_polar(asl, features[0], features[2])
    add_features_delta(asl, features[3])
    add_features_rescaling(asl, features[0], features[4])
    # Display first five rows (pandas data frame) of ASL database, indexed by video and frame
    # asl.df.head()
    return asl

def run_bic(asl, features_ground, words_to_train, min_c, max_c, rand_s):
    # Copied from asl_recognizer.ipynb for IDE debugging using breakpoints.
    # Execute the implementation of SelectorBIC in module my_model_selectors.py
    from my_model_selectors import SelectorBIC

    training = asl.build_training(features_ground)

    print("BIC Available Training words - words: ", training.words)
    print("BIC Quantity of Training words - num_items: ", training.num_items)
    print("BIC Chosen Training words: ", words_to_train)
    print("BIC Chosen Features: ", features_ground)

    sequences = training.get_all_sequences()
    Xlengths = training.get_all_Xlengths()

    for word in words_to_train:
        start = timeit.default_timer()
        model = SelectorBIC(sequences, Xlengths, word,
                            min_n_components=min_c,
                            max_n_components=max_c,
                            random_state = rand_s).select()
        end = timeit.default_timer()-start
        if model is not None:
            print("Training complete for {} with {} states with time {} seconds".format(word, model.n_components, end))
        else:
            print("Training failed for {}".format(word))

def run_dic(asl, features_ground, words_to_train, min_c, max_c, rand_s):
    # Copied from asl_recognizer.ipynb for IDE debugging using breakpoints.
    # Execute the implementation of SelectorDIC in module my_model_selectors.py
    from my_model_selectors import SelectorDIC

    training = asl.build_training(features_ground)

    print("DIC Available Training words - words: ", training.words)
    print("DIC Quantity of Training words - num_items: ", training.num_items)
    print("DIC Chosen Training words: ", words_to_train)
    print("DIC Chosen Features: ", features_ground)

    sequences = training.get_all_sequences()
    Xlengths = training.get_all_Xlengths()
    for word in words_to_train:
        start = timeit.default_timer()
        model = SelectorDIC(sequences, Xlengths, word,
                            min_n_components=min_c,
                            max_n_components=max_c,
                            random_state = rand_s).select()
        end = timeit.default_timer()-start
        if model is not None:
            print("Training complete for {} with {} states with time {} seconds".format(word, model.n_components, end))
        else:
            print("Training failed for {}".format(word))

def run_cv(asl, features_ground, words_to_train, min_c, max_c, rand_s):
    # Copied from asl_recognizer.ipynb for IDE debugging using breakpoints.
    # Execute the implementation of SelectorCV in module my_model_selectors.py
    from my_model_selectors import SelectorCV

    training = asl.build_training(features_ground)

    print("CV Available Training words - words: ", training.words)
    print("CV Quantity of Training words - num_items: ", training.num_items)
    print("CV Chosen Training words: ", words_to_train)
    print("CV Chosen Features: ", features_ground)

    sequences = training.get_all_sequences()
    Xlengths = training.get_all_Xlengths()
    for word in words_to_train:
        start = timeit.default_timer()
        model = SelectorCV(sequences, Xlengths, word,
                            min_n_components=min_c,
                            max_n_components=max_c,
                            random_state = rand_s).select()
        end = timeit.default_timer() - start
        if model is not None:
            print("Training complete for {} with {} states with time {} seconds".format(word, model.n_components, end))
        else:
            print("Training failed for {}".format(word))

def run_demo_selector_constant(asl, features_ground):
    # Copied from asl_recognizer.ipynb for IDE debugging using breakpoints.
    # Execute the implementation of SelectorCV in module my_model_selectors.py
    from my_model_selectors import SelectorConstant

    def train_all_words(features, model_selector):
        # Experiment here with different feature sets defined in Part 1
        training = asl.build_training(features)

        print("SelectorConstant Available Training words - words: ", training.words)
        print("SelectorConstant Quantity of Training words - num_items: ", training.num_items)
        print("SelectorConstant Chosen Features: ", features_ground)

        sequences = training.get_all_sequences()
        Xlengths = training.get_all_Xlengths()
        model_dict = {}
        for word in training.words:
            model = model_selector(sequences, Xlengths, word,
                                   n_constant=3).select()
            model_dict[word] = model
        return model_dict

    models = train_all_words(features_ground, SelectorConstant)
    print("Number of word models returned = {}".format(len(models)))

    test_set = asl.build_test(features_ground)
    print("Number of test set items: {}".format(test_set.num_items))
    print("Number of test set sentences: {}".format(len(test_set.sentences_index)))

def run_my_recognizer(asl, features):
    from my_model_selectors import SelectorConstant
    from my_model_selectors import SelectorCV
    from my_model_selectors import SelectorBIC
    from my_model_selectors import SelectorDIC

    from my_recognizer import recognize
    from asl_utils import show_errors

    def train_all_words(features, model_selector, index):
        training = asl.build_training(features)

        print("Available Training words - words: ", training.words)
        print("Quantity of Training words - num_items: ", training.num_items)
        print("Chosen Training words: All words")

        # Get every fifth element since may be combination of
        # more than one Feature Set (where each Feature Set contains four elements)
        features_abbrev = features[::4]
        chosen_abbrev_list = []
        for i, abbrev in enumerate(features_abbrev):
            chosen_abbrev_list.append(abbrev.split('-')[0])
        chosen = ', '.join(map(str, chosen_abbrev_list))
        print("Chosen Features: ", chosen)

        # print("Chosen Features: ", features[index].split('-')[0])

        print("Chosen Model Selector: ", model_selector.__name__)

        sequences = training.get_all_sequences()

        # Note:
        #
        # training.get_all_Xlengths()
        #
        # This gets the entire db of words in the form of a
        # dictionary of (X, lengths) tuples, and returns two lists
        # for each word:
        # - where X is a numpy array of feature lists
        # (concatenation of all the sequences of frames with the
        #  values of the features i.e. grnd-rx, grnd-lx, ..., over time).
        # The first sequence of frames is 14 frames long, and
        # second is 18 frames long in the example, but only two from each
        # are shown. A sequence of frames corresponds to a succession of
        # movements corresponding to a word
        # - where lengths is a list of lengths of sequences within X
        # (length of the sequences concatenated in the first list)
        #
        # i.e. {'FRANK': (
        #                   array(
        #                       [[ 87, 225],[ 87, 225], ...
        #                       [ 87, 225,  62, 127], [ 87, 225,  65, 128]]
        #                   ),
        #                   [14, 18]
        #                ),
        #      }
        #
        # The first list

        Xlengths = training.get_all_Xlengths()
        words_to_train = training.words
        model_dict = {}

        timeframes = []
        states = []

        for word in words_to_train:
            start = timeit.default_timer()
            model = model_selector(sequences, Xlengths, word,
                                   n_constant=3).select()
            model_dict[word] = model
            end = timeit.default_timer() - start
            if model is not None:
                timeframes.append(end)
                states.append(model.n_components)

                print("Training complete for {} with {} states with time {} seconds".format(word, model.n_components, end))
            else:
                print("Training failed for {}".format(word))

        if timeframes:
            print("Average Timeframe: ", np.mean(timeframes))
        if states:
            print("Average States used: ",  np.mean(states))

        return model_dict

    # features_ground   # Difference between hand and nose locations
    # features_norm     # Fix for different height and arm lengths
    # features_polar    # Fix discontinuity in signing area to prevent interfere with results
    # features_delta    # Speed and direction of hands
    # features_rescaled # Faster and interpretation and analysis of plotted data easier

    # All features
    features_all = features[0] + features[1] + features[2] + features[3] + features[4]

    # All features without norm and polar (i.e. without fixes)
    features_without_norm_and_polar = features[0] + features[3] + features[4]

    # All features without rescaled
    features_without_rescaled = features[0] + features[1] + features[2] + features[3]

    # All features without delta
    features_without_delta = features[0] + features[1] + features[2] + features[4]

    # CHOSEN COMBOS - Choose 3 OFF feature set and model selector combos
    # (16+ combinations all together)

    # Note: Ensure same length of of chosen_features and chosen_model_selectors
    chosen_features = [
        features_all,
            features_all,
                features_all,
                    features_all,
        features_without_norm_and_polar,
            features_without_norm_and_polar,
                features_without_norm_and_polar,
                    features_without_norm_and_polar,
        features_without_rescaled,
            features_without_rescaled,
                features_without_rescaled,
                    features_without_rescaled,
        features_without_delta,
            features_without_delta,
                features_without_delta,
                    features_without_delta,
        features[0],
          features[0],
            features[0],
              features[0],
        features[1],
          features[1],
            features[1],
              features[1],
        features[2],
          features[2],
            features[2],
              features[2],
        features[3],
          features[3],
            features[3],
              features[3],
        features[4],
          features[4],
            features[4],
              features[4]
    ]
    chosen_model_selectors = [
        SelectorConstant,
          SelectorCV,
            SelectorBIC,
              SelectorDIC,
        SelectorConstant,
            SelectorCV,
                SelectorBIC,
                    SelectorDIC,
        SelectorConstant,
            SelectorCV,
                SelectorBIC,
                    SelectorDIC,
        SelectorConstant,
            SelectorCV,
                SelectorBIC,
                    SelectorDIC,
        SelectorConstant,
          SelectorCV,
            SelectorBIC,
              SelectorDIC,
        SelectorConstant,
          SelectorCV,
            SelectorBIC,
              SelectorDIC,
        SelectorConstant,
          SelectorCV,
            SelectorBIC,
              SelectorDIC,
        SelectorConstant,
          SelectorCV,
            SelectorBIC,
              SelectorDIC,
        SelectorConstant,
          SelectorCV,
            SelectorBIC,
              SelectorDIC
    ]

    # Iterate through the 3 OFF interesting combos chosen.
    # Recognize the test set and display the result with the
    # show_errors method
    for index, chosen_feature in enumerate(chosen_features):
        models = train_all_words(chosen_feature, chosen_model_selectors[index], index)
        print("Number of word models returned = {}".format(len(models)))

        test_set = asl.build_test(chosen_feature)
        print("Number of test set items: {}".format(test_set.num_items))
        print("Number of test set sentences: {}".format(len(test_set.sentences_index)))

        probabilities, guesses = recognize(models, test_set)

        # Show the Word Error Rate (WER) and sentence differences in tabular form
        try:
            result = show_errors(guesses, test_set)
        except Exception as e:
            print("Error showing errors: ", e)
        print("Finished processing combo... Trying others if any exist.")

# Imports and runs all Code Cells from Jupyter Notebook files (*.ipynb)
# in current directory whose first 13 characters are `###_DEBUG_IDE`
# so their functions may be called from this .py file
def import_jupyter_notebook_code():
    logging.debug("Registering hooks so Jupyter Notebooks .ipynb importable")
    # Registering hooks so Jupyter Notebooks .ipynb importable
    from notebook_importing import NotebookFinder, NotebookLoader
    # import the .ipynb file
    import asl_recognizer
    from asl_recognizer import test
    asl_recognizer.test()

# Note: Alternative is to within the .ipynb file and save it as a .py file
# and then import it with `asl_recognizer`
def run():
    try:
        import_jupyter_notebook_code()

        # Feature Sets

        # Feature that takes the differences between hand and nose locations
        features_ground = ['grnd-rx', 'grnd-ry', 'grnd-lx', 'grnd-ly']

        # Feature that accounts for signers with different heights and arm length
        features_norm = ['norm-rx', 'norm-ry', 'norm-lx', 'norm-ly']

        # Feature that fixes discontinuity that occurs directly to the left of the
        # signers nose, which may be in the signing area and interfere with results.
        # The feature moves the discontinuity to directly above the signers head,
        # an area not generally used in signing
        features_polar = ['polar-rr', 'polar-rtheta', 'polar-lr', 'polar-ltheta']

        # Feature representing difference in values between one frame and the next frames
        features_delta = ['delta-rx', 'delta-ry', 'delta-lx', 'delta-ly']

        features_rescaled = ['right-x-rescaled', 'right-y-rescaled', 'left-x-rescaled', 'left-y-rescaled']

        features = [
                    features_ground,   # Difference between hand and nose locations
                    features_norm,     # Fix for different height and arm lengths
                    features_polar,    # Fix discontinuity in signing area to prevent interfere with results
                    features_delta,    # Speed and direction of hands
                    features_rescaled  # Faster and interpretation and analysis of plotted data easier
                    ]

        # Initalise ASLDB and Add Feature Sets
        asl = initialise_asl_db(features)

        # PART 2

        words_to_train = ['FISH', 'BOOK', 'VEGETABLE', 'FUTURE', 'JOHN']

        min_c = 2   # default 2
        max_c = 15   # default 15
        rand_s = 14 # default 14

        # logging.debug("Recogniser calling BIC Model Selector")
        # run_bic(asl, features_ground, words_to_train, min_c, max_c, rand_s)
        #
        # logging.debug("Recogniser calling DIC Model Selector")
        # run_dic(asl, features_ground, words_to_train, min_c, max_c, rand_s)
        #
        # logging.debug("Recogniser calling CV Model Selector")
        # run_cv(asl, features_ground, words_to_train, min_c, max_c, rand_s)

        # PART 3 - Analyze WER performance of different combo of feature sets and model selectors

        # logging.debug("Recogniser calling SelectorConstant Model Selector")
        # run_demo_selector_constant(asl, features_ground)

        logging.debug("MyRecognizer")

        # Instructions:
        #
        # Choose Feature Set:
        #  - features_ground
        #  - features_norm
        #  - features_polar
        #  - features_delta
        #
        # Choose Model Selector Technique:
        #  - SelectorConstant
        #  - CV
        #  - BIC
        #  - DIC

        run_my_recognizer(asl, features)

    except SystemExit:
        logging.exception('SystemExit occurred')
    except KeyError as e:
        cause = e.args[0]
        logging.exception('Exception KeyError caused by: ', cause)
    except Exception as e:
        logging.exception('Exception occurred: ', e)

if __name__ == '__main__':
    run()