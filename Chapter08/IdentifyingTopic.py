from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from gensim import corpora, models
import nltk
import feedparser

class IdentifyingTopicExample:
    def getDocuments(self):
        url = 'https://sports.yahoo.com/mlb/rss.xml'
        feed = feedparser.parse(url)
        self.documents = []
        for entry in feed['entries'][:5]:
            text = entry['summary']
            if 'ex' in text:
                continue
            self.documents.append(text)
            print("-- {}".format(text))
        print("INFO: Fetching documents from {} completed".format(url))

    def cleanDocuments(self):
        tokenizer = RegexpTokenizer(r'[a-zA-Z]+')
        en_stop = set(stopwords.words('english'))
        self.cleaned = []
        for doc in self.documents:
            lowercase_doc = doc.lower()
            words = tokenizer.tokenize(lowercase_doc)
            non_stopped_words = [i for i in words if not i in en_stop]
            self.cleaned.append(non_stopped_words)
        print("INFO: Clearning {} documents completed".format(len(self.documents)))

    def doLDA(self):
        dictionary = corpora.Dictionary(self.cleaned)
        corpus = [dictionary.doc2bow(cleandoc) for cleandoc in self.cleaned]
        ldamodel = models.ldamodel.LdaModel(corpus, num_topics=2, id2word = dictionary)
        print(ldamodel.print_topics(num_topics=2, num_words=4))

    def run(self):
        self.getDocuments()
        self.cleanDocuments()
        self.doLDA()

if __name__ == '__main__':
    topicExample = IdentifyingTopicExample()
    topicExample.run()
