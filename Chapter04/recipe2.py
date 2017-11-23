import re

def text_match(text, patterns):
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print("Pattern to test start and end with")
print(text_match("abbc", "^a.*c$"))

print("Begin with a word")
print(text_match("Tuffy eats pie, Loki eats peas!", "^\w+"))

print("End with a word and optional punctuation")
print(text_match("Tuffy eats pie, Loki eats peas!", "\w+\S*?$"))

print("Finding a word which contains character, not start or end of the word")
print(text_match("Tuffy eats pie, Loki eats peas!", "\Bu\B"))