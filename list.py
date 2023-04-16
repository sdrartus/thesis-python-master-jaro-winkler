import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
from pyjarowinkler import distance

# Download the stop words and lemmatization data
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('punkt')

# Define a list of profane words and their euphemisms
profanity = {
    "fuck": "fudge",
    "shit": "shoot",
    "damn": "darn",
    "ass": "bum",
    "bitch": "witch",
    "crap": "crud"
}

# Define a leet dictionary for converting leet speak to regular text
leet = {
    "1": "i",
    "3": "e",
    "4": "a",
    "5": "s",
    "7": "t",
    "0": "o",
    "@" :"a",
    "/\ ": "a",
    "/-\ ": "a",
    "*" : "a",
    "ä" : "a",
    "á" :"a",
    "à" : "a",
    "â" : "a",
    "a^": "a",
    "ã" : "a",
    "å" : "a",
    "ą" : "a",
    "ª" : "a",
    "∀" : "a",
    "∧" : "a",
    "α" : "a",
    "8" : "b",
    "|3": "b",
    "13": "b",
    "ß" : "b",
    "þ" : "b",
    "v" : "b",
    "ć" : "c",
    "č" : "c",
    "ç" : "c",
    "©" : "c",
    "σ" : "c",
    "(" : "c",
    "¢" : "c",
    "<" : "c",
    '[' : "c",
    '©': "c",
    "[)" : "d",
    "|>" : "d",
    "|)" : "d",
    "|]": "d",
    "3" : "e",
    "€" : "e",
    "є" : "e",
    "[-": "e",
    "|=" : "f",
    "ƒ" : "f",
    "/=": "f",
    "6" : "g",
    "(_+": "g",
    "#" : "h",
    "/-/" : "h",
    "[-]" : "h",
    "]-[" : "h",
    ")-(" : "h",
    "(-)" : "h",
    ":-:" : "h",
    "|~|" : "h",
    "|-|" : "h",
    "]~[" : "h",
    "}{" : "h",
    "1" : "i",
    '!' : "i",
    "|" : "i",
    "][" : "i",
    "]" : "i",
    ":": "i",
    "_|" : "j",
    "_/" : "j",
    "¿" : "j",
    "(/" : "j",
    "ʝ" : "j",
    ";" : "j",
    "X" : "k",
    "|<" : "k",
    "|{" : "k",
    "ɮ" : "k",
    "£" : "l",
    "1_" : "l",
    "ℓ" : "l",
    "|_" : "l",
    "[_": "l",
    "|V|" : "m",
    "|\/|" : "m",
    "/\/\ " : "m",
    "/V\ ": "m",
    "|V" : "n",
    "|\|" : "n",
    "/\/" : "n",
    "[\]" : "n",
    "/V" : "n",
    "[]" : "o",
    "0" :"o" ,
    "()" : "o",
    "°" : "o",
    "|*" : "p",
    "|o" : "p",
    "|º" : "p",
    "|°" : "p",
    "/*" : "p",
    "¶" : "q",
    "(_,)" : "q",
    "()_" : "q",
    "0_" : "q",
    "°|" : "q",
    "<|" : "q",
    "®" : "r",
    "2" : "r",
    "|?" : "r",
    "/2" : "r",
    "®" : "r",
    "Я" : "r",
    "|2": "r",
    "§" : "s",
    "5" : "s",
    "$" : "s",
    "_/¯": "s",
    "7" : "t",
    "†" : "t",
    "¯|¯" : "t",
    "(_)" : "u",
    "|_|" : "u",
    "L|" : "u",
    "µ": "u",
    "\/" : "v",
    "|/" : "v",
    "\/\/" : "w",
    "vv" : "w",
    "\//" :"w",
    "\^/" : "w",
    "\V/" : "w",
    "\|/" : "w",
    "\_|_/" : "w",
    "\_:_/" : "w",
    "><": "x",
    "}{" : "x",
    "×" : "x",
    ")(" : "x",
    " `/" : "y",
    "φ" : "y",
    "¥" : "y",
    "\/": "y",
    "≥" : "z",
    "7_" : "z",
    ">_": "z"
}


# Text Processing Function
def process_text(text):
    newval = "new value"
    # Convert leet speak to regular text
    for key, value in leet.items():
        text = text.replace(key, value)
    # if text in leet:
    #     values = leet[text]
    #     for i in range(len(values)):
    #         if values[i] == text:
    #             values[i] = newval

    # Normalize the text
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)

    # Tokenize the text
    tokens = nltk.word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]

    # Perform stemming and lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Check for profanity and replace with euphemisms
    for i, token in enumerate(tokens):
        if token in profanity:
            euphemism = max(profanity, key=lambda x: distance.get_jaro_distance(token, x))
            stemmed_tokens[i] = euphemism
            lemmatized_tokens[i] = euphemism

    # Convert the tokens back to a string
    stemmed_text = " ".join(stemmed_tokens)
    lemmatized_text = " ".join(lemmatized_tokens)

    return stemmed_text, lemmatized_text


# Example usage
# text = "I f0cking hate this sh1t, it's so d@mn annoying."
# stemmed_text, lemmatized_text = process_text(text)
# print("Stemmed text:", stemmed_text)
# print("Lemmatized text:", lemmatized_text)
