import nltk
import sys

"""
sentence = "Satya Nadella is the CEO of Microsoft."

words = nltk.word_tokenize(sentence)

tagged = nltk.pos_tag(words)

chunks = nltk.ne_chunk(tagged, binary=True)

print(tagged)
print(chunks)

sys.exit(0)

print(nltk.tree2conlltags(nltk.ne_chunk(tagged)))

grammar = r"NAMED-ENTITY: {<NNP>+}"
cp = nltk.RegexpParser(grammar)
print(cp.parse(tagged))
"""

grammar = r"NAMED-ENTITY: {<NNP>+}"
cp = nltk.RegexpParser(grammar)

samplestrings = [
    "Microsoft Azure is a cloud service",
    "Bill Gates announces Satya Nadella as new CEO of Microsoft"
]

def demo(samplestrings):
    for s in samplestrings:
        words = nltk.word_tokenize(s)
        tagged = nltk.pos_tag(words)
        # chunks = nltk.ne_chunk(tagged)
        chunks = cp.parse(tagged)
        print(nltk.tree2conllstr(chunks))
        print(chunks)

demo(samplestrings)

strings = ["""
Microsoft NNP B-COMPANY
Azure NNP I-CLOUDSERVICE
is VBZ O
a DT O
cloud JJ O
service NN O
""", """
Bill NNP B-PERSON
Gates NNP I-PERSON
announces NNS O
Satya NNP B-PERSON
Nadella NNP I-PERSON
as IN O
new JJ O
CEO NNP B-NAMED-ENTITY
of IN O
Microsoft NNP B-COMPANY
"""]

#print(nltk.conllstr2tree(strings[1]))
#print(nltk.ne_chunk(nltk.conllstr2tree(strings[1])))


