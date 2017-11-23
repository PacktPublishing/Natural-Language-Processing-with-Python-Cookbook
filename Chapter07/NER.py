import nltk

def sampleNE():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent))

def sampleNE2():
    sent = nltk.corpus.treebank.tagged_sents()[0]
    print(nltk.ne_chunk(sent, binary=True))

if __name__ == '__main__':
    sampleNE()
    sampleNE2()
