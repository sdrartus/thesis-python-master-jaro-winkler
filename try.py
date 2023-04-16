import re
import math
from collections import Counter

import re
from difflib import SequenceMatcher

# Define profanity dictionary
# profanity_dict = {
#     'fuck': ['fudge', 'frick', 'freak'],
#     'shit': ['shoot', 'crud', 'poo'],
#     'ass': ['butt', 'rear', 'derriere']
# }
#
# # Define Jaro similarity algorithm
# def jaro_similarity(s1, s2):
#     # implementation goes here
#     # implementation of Jaro similarity algorithm
#     len_s1 = len(s1)
#     len_s2 = len(s2)
#
#     if len_s1 == 0 or len_s2 == 0:
#         return 0.0
#
#     if len_s1 > len_s2:
#         max_dist = len_s1 // 2 - 1
#     else:
#         max_dist = len_s2 // 2 - 1
#
#     s1_matches = [False] * len_s1
#     s2_matches = [False] * len_s2
#
#     matches = 0
#     transpositions = 0
#
#     for i in range(len_s1):
#         start = max(0, i - max_dist)
#         end = min(i + max_dist + 1, len_s2)
#         for j in range(start, end):
#             if s2_matches[j]:
#                 continue
#             if s1[i] != s2[j]:
#                 continue
#             s1_matches[i] = True
#             s2_matches[j] = True
#             matches += 1
#             break
#
#     if matches == 0:
#         return 0.0
#
#     k = 0
#     for i in range(len_s1):
#         if not s1_matches[i]:
#             continue
#         while not s2_matches[k]:
#             k += 1
#         if s1[i] != s2[k]:
#             transpositions += 1
#         k += 1
#
#     sim = (matches / len_s1 + matches / len_s2 + (matches - transpositions / 2) / matches) / 3
#     return sim
#
#
# # Define function to get euphemism with highest Jaro similarity
# def get_best_euphemism(profane_word, euphemisms):
#     best_euphemism = ''
#     best_score = 0
#     for euphemism in euphemisms:
#         score = jaro_similarity(profane_word, euphemism)
#         if score is not None and score > best_score:
#             best_euphemism = euphemism
#             best_score = score
#     return best_euphemism
#
# # Define function to filter profanity  + word[-3:] +
# def filter_profanity(text):
#     words = re.findall(r'\b\w+\b', text)
#     filtered_words = []
#     for word in words:
#         if word.lower() in profanity_dict:
#             euphemisms = profanity_dict[word.lower()]
#             best_euphemism = get_best_euphemism(word, euphemisms)
#             suffix = re.findall(r'\b\w+(' r')\b', text)
#             if suffix:
#                 if best_euphemism != '':
#                     filtered_words.append(best_euphemism + suffix[0][-3:])
#                 else:
#                     filtered_words.append(word)
#             else:
#                 filtered_words.append(best_euphemism)
#         else:
#             filtered_words.append(word)
#     filtered_text = ' '.join(filtered_words)
#     return filtered_text



# import re

profanity_dict = {
    "crap": ["poop", "doodoo", "frap", "number two"],
    "fuck": ["freak", "flip", "fudge"],
    "damn": ["darn", "dang", "heck"],
    "butt" : ["bum", "derriere"]
}

def replace_profanity(match):
    word = match.group(0)
    if word in profanity_dict:
        return profanity_dict[word]
    # elif "fuck" in word:
    #     return "freak" + word[word.index("fuck")+4:]
    else:
        return word

# Original
# def replace_profanity(match):
#     word = match.group(0)
#     if word in profanity_dict:
#         return profanity_dict[word]
#     # elif "fuck" in word:
#     #     return "freak" + word[word.index("fuck")+4:]
#     else:
#         return word

def filter_profanity(text):
    filtered_text = text
    for profanity in profanity_dict.keys():
        pattern = re.compile(re.escape(profanity), re.IGNORECASE)

        euphemisms = profanity_dict[text.lower()]
        jw_similarities = [SequenceMatcher(None, text.lower(), euph.lower()).ratio() for euph in euphemisms]
        max_jw_similarity_index = jw_similarities.index(max(jw_similarities))
        max_jw_euphemism = euphemisms[max_jw_similarity_index]
        filtered_text = pattern.sub(max_jw_euphemism, filtered_text)
    return filtered_text


# Original filter profanity
# def filter_profanity(text):
#     filtered_text = text
#     for profanity in profanity_dict.keys():
#         pattern = re.compile(re.escape(profanity), re.IGNORECASE)
#         filtered_text = pattern.sub(replace_profanity, filtered_text)
#     return filtered_text


input_text = "I love shitingggg's ice cream. This is a fucking stupid idea, you asshole. It's damning hot today!"
output_text = filter_profanity(input_text)
print(output_text)

# text = "I can't believe you said that shitting. What the fuck is wrong with you?"
# filtered_text = filter_profanity(text)
# print(filtered_text)
# # Output: "I can't believe you said that shoot. What the fudge is wrong with you?"
