# from lxml import html
import requests
from bs4 import BeautifulSoup
import nltk

x = requests.get('https://pythonprogramming.net')
soup = BeautifulSoup(x.content, "html.parser")
soup_text = soup.get_text()
tokens = nltk.word_tokenize(soup_text)


user_input = 'Programming'
count = 0
for word in tokens:
    if word == user_input:
        count+=1

print(count)