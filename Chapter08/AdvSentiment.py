import nltk
import nltk.sentiment.util
import nltk.sentiment.sentiment_analyzer
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def mySentimentAnalyzer():
    def score_feedback(text):
        positive_words = ['love', 'genuine', 'liked']
        if '_NEG' in ' '.join(nltk.sentiment.util.mark_negation(text.split())):
            score = -1
        else:
            analysis = nltk.sentiment.util.extract_unigram_feats(text.split(), positive_words)
            if True in analysis.values():
                score = 1
            else:
                score = 0
        return score

    feedback = """I love the items in this shop, very genuine and quality is well maintained.
    I have visited this shop and had samosa, my friends liked it very much.
    ok average food in this shop.
    Fridays are very busy in this shop, do not place orders during this day."""
    print(' -- custom scorer --')
    for text in feedback.split("\n"):
        print("score = {} for >> {}".format(score_feedback(text), text))


def advancedSentimentAnalyzer():
    sentences = [
        ':)',
        ':(',
        'She is so :(',
        'I love the way cricket is played by the champions',
        'She neither likes coffee nor tea',
    ]
    senti = SentimentIntensityAnalyzer()
    print(' -- built-in intensity analyser --')
    for sentence in sentences:
        print('[{}]'.format(sentence), end=' --> ')
        kvp = senti.polarity_scores(sentence)
        for k in kvp:
            print('{} = {}, '.format(k, kvp[k]), end='')
        print()

if __name__ == '__main__':
    advancedSentimentAnalyzer()
    mySentimentAnalyzer()
