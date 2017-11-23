import nltk

text = "Ravi is the CEO of a Company. He is very powerful public speaker also."

grammar = '\n'.join([
    'NP: {<DT>*<NNP>}',
    'NP: {<JJ>*<NN>}',
    'NP: {<NNP>+}',
])

sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    tags = nltk.pos_tag(words)
    chunkparser = nltk.RegexpParser(grammar)
    result = chunkparser.parse(tags)
    print(result)
