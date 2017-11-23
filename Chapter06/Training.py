import nltk
from nltk.corpus import conll2000

sentence = "Ravi is the CEO of a Company."

def myParser():
    grammar = '\n'.join([
	'NP: {<DT>*<NNP>}',
	'NP: {<JJ>*<NN>}',
	'NP: {<NNP>+}',
	])
    return nltk.RegexpParser(grammar)

def buildIOBTags(text):
    chunkparser = myParser()
    words = nltk.word_tokenize(text)
    postags = nltk.pos_tag(words)
    tree = chunkparser.parse(postags)
    # This whole thing can be replaced by
    # nltk.chunk.tree2conlltags(tree) function
    # which returns 3 tuple
    return nltk.chunk.tree2conlltags(tree)
"""
    for subtree in tree:
	if type(subtree) is not tuple:
	    tokenPosition = 0
	    for token in subtree.leaves():
		if tokenPosition == 0:
		    print(' '.join([token[0], token[1], 'B-{}'.format(subtree.label())]))
		else:
		    print(' '.join([token[0], token[1], 'I-{}'.format(subtree.label())]))
		tokenPosition = tokenPosition + 1
	else:
	    token = subtree
	    print(' '.join([token[0], token[1], 'O']))
    """

def test_baseline():
    cp = nltk.RegexpParser("")
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    # print(len(test_sents[0]))
    # print(test_sents[0])
    print(cp.evaluate(test_sents))

def test_regexp():
    grammar = r"NP: {<[CDJNP].*>+}"
    cp = nltk.RegexpParser(grammar)
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    print(cp.evaluate(test_sents))

def test_myparser():
    parser = myParser()
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    print(parser.evaluate(test_sents))

class BigramChunker(nltk.ChunkParserI):
    def __init__(self, train_sents):
        train_data = [[(t,c) for w,t,c in nltk.chunk.tree2conlltags(sent)] for sent in train_sents]
        self.tagger = nltk.BigramTagger(train_data)

    def parse(self, sentence):
        pos_tags = [pos for (word,pos) in sentence]
        tagged_pos_tags = self.tagger.tag(pos_tags)
        chunktags = [chunktag for (pos, chunktag) in tagged_pos_tags]
        conlltags = [(word, pos, chunktag) for ((word,pos),chunktag)
                in zip(sentence, chunktags)]
        return nltk.chunk.conlltags2tree(conlltags)

def test_mychunker():
    test_sents = conll2000.chunked_sents('test.txt', chunk_types=['NP'])
    train_sents = conll2000.chunked_sents('train.txt', chunk_types=['NP'])
    my_chunker = BigramChunker(train_sents)
    print(my_chunker.evaluate(test_sents))


#test_baseline()
#test_myparser()
test_regexp()
test_mychunker()
