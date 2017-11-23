import re

street = '21 Ramkrishna Road'
print(re.sub('Road', 'Rd', street))

text = 'Diwali is a festival of light, Holi is a festival of color!'
print(re.findall(r"\b\w{5}\b", text))