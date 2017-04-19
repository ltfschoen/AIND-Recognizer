import warnings
from asl_data import SinglesData

import logging

def recognize(models: dict, test_set: SinglesData):
    """ Recognize test word sequences from word models set

    :param models: dict of trained models
       {'SOMEWORD': GaussianHMM model object, 'SOMEOTHERWORD': GaussianHMM model object, ...}
    :param test_set: SinglesData object
    :return: (list, list)  as probabilities, guesses
       both lists are ordered by the test set word_id
       probabilities is a list of dictionaries where each key a word and value is Log Liklihood
           [{SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            {SOMEWORD': LogLvalue, 'SOMEOTHERWORD' LogLvalue, ... },
            ]
       guesses is a list of the best guess words ordered by the test set word_id
           ['WORDGUESS0', 'WORDGUESS1', 'WORDGUESS2',...]
    """
    warnings.filterwarnings("ignore", category=DeprecationWarning)

    def calc_best_score(word_log_likelihoods):
        # Max of dictionary of values by comparing each item by value at index
        return max(word_log_likelihoods, key = word_log_likelihoods.get)
        # return max(word_log_likelihoods, key = lambda index: word_log_likelihoods[index])

    logging.debug("My Recognizer Started...")

    probabilities = []
    guesses = []

    # Iterate through each item in the Test Set
    for word_id in range(0, len(test_set.get_all_Xlengths())):
        current_word_feature_lists_sequences, current_sequences_length = test_set.get_item_Xlengths(word_id)
        word_log_likelihoods = {}

        # Calculate Log Likelihood score for each word and model and append to probability list
        for word, model in models.items():
            try:
                score = model.score(current_word_feature_lists_sequences, current_sequences_length)
                word_log_likelihoods[word] = score
            except:
                # Eliminate non-viable models from consideration
                word_log_likelihoods[word] = float("-inf")
                continue
        # Probabilities appended with probability list
        probabilities.append(word_log_likelihoods)
        # Guesses appended with calculation of word with maximum score (log likelihood) for each model
        guesses.append(calc_best_score(word_log_likelihoods))

    return probabilities, guesses

