import nltk
import string
from nltk.parse.generate import generate

productions = [
    "ROOT -> WORD",
    "WORD -> ' '",
    "WORD -> NUMBER LETTER",
    "WORD -> LETTER NUMBER",
]

digits = list(string.digits)
for digit in digits[:4]:
    productions.append("NUMBER -> '{w}'".format(w=digit))

letters = "' | '".join(list(string.ascii_lowercase)[:4])
productions.append("LETTER -> '{w}'".format(w=letters))

grammarString = "\n".join(productions)

grammar = nltk.CFG.fromstring(grammarString)

print(grammar)

for sentence in generate(grammar, n=5, depth=5):
    palindrome = "".join(sentence).replace(" ", "")
    print("Generated Word: {}, Size : {}".format(palindrome, len(palindrome)))
