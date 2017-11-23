import re

#search for literal strings in sentence
patterns = [ 'Tuffy', 'Pie', 'Loki' ]
text = 'Tuffy eats pie, Loki eats peas!'
for pattern in patterns:
    print('Searching for "%s" in "%s" ->' % (pattern, text),)
    if re.search(pattern,  text):
        print('Found!')
    else:
        print('Not Found!')

#search a substring and find it's location too

text = 'Diwali is a festival of lights, Holi is a festival of colors!'
pattern = 'festival'
for match in re.finditer(pattern, text):
    s = match.start()
    e = match.end()
    print('Found "%s" at %d:%d' % (text[s:e], s, e))