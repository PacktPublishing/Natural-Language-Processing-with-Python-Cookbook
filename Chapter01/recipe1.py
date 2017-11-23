from nltk.corpus import reuters

files = reuters.fileids()
print(files)

words16097 = reuters.words(['test/16097'])
print(words16097)

words20 = reuters.words(['test/16097'])[:20]
print(words20)


reutersGenres = reuters.categories()
print(reutersGenres)


for w in reuters.words(categories=['bop','cocoa']):
    print(w+' ',end='')
    if(w is '.'):
        print()
