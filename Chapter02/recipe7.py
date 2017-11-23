from bs4 import BeautifulSoup

html_doc = open('sample-html.html', 'r').read()
soup = BeautifulSoup(html_doc, 'html.parser')

print('Full text HTML Stripped:')
print(soup.get_text())

print('Accessing the <title> tag :', end=' ')
print(soup.title)

print('Accessing the text of <H1> tag :', end=' ')
print(soup.h1.string)

print('Accessing property of <img> tag :', end=' ')
print(soup.img['alt'])

print('\nAccessing all occurences of the <p> tag :')
for p in soup.find_all('p'):
    print(p.string)