import re

def stem(word):
    splits = re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', word)
    stem = splits[0][0]
    return stem

raw = "Keep your friends close, but your enemies closer."
tokens = re.findall(r'\w+|\S\w*', raw)
print(tokens)

for t in tokens:
    print("'"+stem(t)+"'")