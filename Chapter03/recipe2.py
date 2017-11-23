from nltk import PorterStemmer, LancasterStemmer, word_tokenize

raw = "My name is Maximus Decimus Meridius, commander of the Armies of the North, General of the Felix Legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

porter = PorterStemmer()
pStems = [porter.stem(t) for t in tokens]
print(pStems)

lancaster = LancasterStemmer()
lStems = [lancaster.stem(t) for t in tokens]
print(lStems)