import processText
import main
import try_again
from try_again import filter_profanity
from try_again import leet_conver

def cleanText(mess):
    # proc = processText.processText(mess)
    processed = leet_conver(mess)
    # clean_text = filter_profanity(processed)
    pas = filter_profanity(processed)
    return pas
