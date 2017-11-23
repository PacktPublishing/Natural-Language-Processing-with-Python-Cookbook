import re

raw = "I am big! It's the pictures that got small."
print(re.split(r' +', raw))

print(re.split(r'\W+', raw))

print(re.findall(r'\w+|\S\w*', raw))