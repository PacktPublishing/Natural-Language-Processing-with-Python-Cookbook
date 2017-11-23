from nltk import word_tokenize, PorterStemmer, WordNetLemmatizer

raw = "My name is Maximus Decimus Meridius, commander of the armies of the north, General of the Felix legions and loyal servant to the true emperor, Marcus Aurelius. Father to a murdered son, husband to a murdered wife. And I will have my vengeance, in this life or the next."
tokens = word_tokenize(raw)

porter = PorterStemmer()
stems = [porter.stem(t) for t in tokens]
print(stems)

lemmatizer = WordNetLemmatizer()
lemmas = [lemmatizer.lemmatize(t) for t in tokens]
print(lemmas)