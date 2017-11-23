import re

url= "http://www.telegraph.co.uk/formula-1/2017/10/28/mexican-grand-prix-2017-time-does-start-tv-channel-odds-lewis1/2017/05/12/"
date_regex = '/(\d{4})/(\d{1,2})/(\d{1,2})/'

print("Date found in the URL :", re.findall(date_regex, url))


def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450."))
print(is_allowed_specific_char("*&%@#!}{"))