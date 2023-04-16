import re
from difflib import SequenceMatcher


from processText import processText

profanity_dict = {
    "crap": ["poop", "doodoo", "frap", "number two"],
    "fuck": ["freak", "flip", "fudge"],
    "damn": ["darn", "dang", "heck"],
    "butt" : ["bum", "derriere"]
}

def filter_profanity(raw_text):
    # Iterate over each word in the raw text
    for word in re.findall(r'\w+', raw_text):
        # Check if the word is a profanity
        if word.lower() in profanity_dict:
            # Find the euphemism with the highest Jaro-Winkler similarity
            euphemisms = profanity_dict[word.lower()]
            jw_similarities = [SequenceMatcher(None, word.lower(), euph.lower()).ratio() for euph in euphemisms]
            max_jw_similarity_index = jw_similarities.index(max(jw_similarities))
            max_jw_euphemism = euphemisms[max_jw_similarity_index]

            # Replace the profanity with the euphemism
            raw_text = re.sub(r'\b{}\b'.format(word), max_jw_euphemism, raw_text, flags=re.IGNORECASE)

    return raw_text

#
# raw_text = "I said a cr@p d@mn. I shouldn't have said it. I fUck f0ck bad."
# processed = processText(raw_text)
# clean_text = filter_profanity(processed)
# print(processed)
# print(clean_text)





