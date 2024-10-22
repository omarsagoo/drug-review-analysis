import re
import sys
sys.path.append("./utils")

# import local constants and helpers. See Appendix C for Keywords.
from keywords import side_effect_keywords, negation_words
# See Appendix D for parser.
from parser import parse_string, find_first_occurence

def check_for_negation(text, keyword):
    words = text.split()
    keyword_index = find_first_occurence(keyword, words)

    if keyword_index == -1:
        return False

    # Search for negation within the 3 words before the keyword
    window = words[max(0, keyword_index - 3): keyword_index]

    # iterate through the negation words and check if any of them are found in the window.
    for negation in negation_words:
        if any(negation in word for word in window):
            return True
    return False

# Create a function to check if the review mentions side effects or no side effects
def check_side_effects(review):
    if review == '': 
        return 0

    review = parse_string(review) # Convert the review to lowercase

    # Search for any of the keywords in the review
    for keyword in side_effect_keywords:
        # Search for the keyword as a whole word using regular expressions
        if re.search(re.escape(keyword), review):
            # If the keyword is found, check for negation
            if not check_for_negation(review, keyword):
                return 1  # Side effect found and not negated
    return 0  # No side effects mentioned or negated
