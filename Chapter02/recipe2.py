str = 'NLTK Dolly Python'
print('Substring ends at:',str[:4])

print('Substring starts from:',str[11:] )
print('Substring :',str[5:10])
print('Substring fancy:', str[-12:-7])

if 'NLTK' in str:
    print('found NLTK')

replaced = str.replace('Dolly', 'Dorothy')
print('Replaced String:', replaced)

print('Accessing each character:')
for s in replaced:
    print(s)