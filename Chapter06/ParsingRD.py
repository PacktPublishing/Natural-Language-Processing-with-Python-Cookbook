import nltk

def RDParserExample(grammar, textlist):
    parser = nltk.parse.RecursiveDescentParser(grammar)
    for text in textlist:
        sentence = nltk.word_tokenize(text)
        for tree in parser.parse(sentence):
            print(tree)
            tree.draw()

grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> NNP VBZ
VP -> IN NNP | DT NN IN NNP
NNP -> 'Tajmahal' | 'Agra' | 'Bangalore' | 'Karnataka'
VBZ -> 'is'
IN -> 'in' | 'of'
DT -> 'the'
NN -> 'capital'
""")

text = [
    "Tajmahal is in Agra",
    "Bangalore is the capital of Karnataka",
]

RDParserExample(grammar, text)
