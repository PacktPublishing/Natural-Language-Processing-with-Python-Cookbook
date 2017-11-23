import nltk
from nltk.corpus import webtext
print(webtext.fileids())

fileid = 'singles.txt'
wbt_words = webtext.words(fileid)
fdist = nltk.FreqDist(wbt_words)

print('Count of the maximum appearing word "',fdist.max(),'" : ', fdist[fdist.max()])
print('Total Number of distinct tokens in the bag : ', fdist.N())
print('Following are the most common 10 words in the bag')
print(fdist.most_common(10))
print('Frequency Distribution on Personal Advertisements')
print(fdist.tabulate())
fdist.plot(cumulative=True)