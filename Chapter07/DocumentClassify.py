import nltk
import random
import feedparser

urls = {
    'mlb': 'https://sports.yahoo.com/mlb/rss.xml',
    'nfl': 'https://sports.yahoo.com/nfl/rss.xml',
}

feedmap = {}
stopwords = nltk.corpus.stopwords.words('english')

def featureExtractor(words):
    features = {}
    for word in words:
        if word not in stopwords:
            features["word({})".format(word)] = True
    return features

sentences = []

for category in urls.keys():
    feedmap[category] = feedparser.parse(urls[category])
    print("downloading {}".format(urls[category]))
    for entry in feedmap[category]['entries']:
        data = entry['summary']
        words = data.split()
        sentences.append((category, words))

featuresets = [(featureExtractor(words), category) for category, words in sentences]
random.shuffle(featuresets)

total = len(featuresets)
off = int(total/2)
trainset = featuresets[off:]
testset = featuresets[:off]

classifier = nltk.NaiveBayesClassifier.train(trainset)

print(nltk.classify.accuracy(classifier, testset))

classifier.show_most_informative_features(5)
for (i, entry) in enumerate(feedmap['nfl']['entries']):
    if i < 4:
        features = featureExtractor(entry['title'].split())
        category = classifier.classify(features)
        print('{} -> {}'.format(category, entry['summary']))

