import nltk
import random

sampledata = [
    ('KA-01-F 1034 A', 'rtc'),
    ('KA-02-F 1030 B', 'rtc'),
    ('KA-03-FA 1200 C', 'rtc'),
    ('KA-01-G 0001 A', 'gov'),
    ('KA-02-G 1004 A', 'gov'),
    ('KA-03-G 0204 A', 'gov'),
    ('KA-04-G 9230 A', 'gov'),
    ('KA-27 1290', 'oth')
]
random.shuffle(sampledata)
testdata = [
    'KA-01-G 0109',
    'KA-02-F 9020 AC',
    'KA-02-FA 0801',
    'KA-01 9129'
]
def learnSimpleFeatures():
    def vehicleNumberFeature(vnumber):
        return {'vehicle_class': vnumber[6]}
    featuresets = [(vehicleNumberFeature(vn), cls) for (vn, cls) in sampledata]
    classifier = nltk.NaiveBayesClassifier.train(featuresets)
    for num in testdata:
        feature = vehicleNumberFeature(num)
        print("(simple) %s is of type %s" %(num, classifier.classify(feature)))

def learnFeatures():
    def vehicleNumberFeature(vnumber):
        return {
            'vehicle_class': vnumber[6],
            'vehicle_prev': vnumber[5]
        }
    featuresets = [(vehicleNumberFeature(vn), cls) for (vn, cls) in sampledata]
    classifier = nltk.NaiveBayesClassifier.train(featuresets)
    for num in testdata:
        feature = vehicleNumberFeature(num)
        print("(dual) %s is of type %s" %(num, classifier.classify(feature)))

learnSimpleFeatures()
learnFeatures()
