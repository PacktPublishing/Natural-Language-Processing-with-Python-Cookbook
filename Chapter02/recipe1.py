namesList = ['Tuffy','Ali','Nysha','Tim' ]
sentence = 'My dog sleeps on sofa'

names = ';'.join(namesList)
print(type(names), ':', names)
wordList = sentence.split(' ')
print((type(wordList)), ':', wordList)

additionExample = 'ganehsa' + 'ganesha' + 'ganesha'
multiplicationExample = 'ganesha' * 2
print('Text Additions :', additionExample)
print('Text Multiplication :', multiplicationExample)

str = 'Python NLTK'
print(str[1])
print(str[-3])