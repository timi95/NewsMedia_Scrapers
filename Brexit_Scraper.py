import re #RegularExpression Module
import requests
from bs4 import BeautifulSoup
import nltk
# nltk.download('averaged_perceptron_tagger')



Target_Sites = [
'http://www.dailymail.co.uk',
'http://www.telegraph.co.uk',
'http://www.independent.co.uk',
'http://www.mirror.co.uk',
'http://www.thesun.co.uk',
'http://www.Express.co.uk',
'http://www.express.co.uk',
'http://www.metro.co.uk',
'http://www.huffingtonpost.co.uk',
'http://www.standard.co.uk',
'http://www.manchestereveningnews.co.uk',
'http://www.pinknews.co.uk',
'http://www.wired.co.uk',
'http://www.dailyrecord.co.uk',
'http://www.walesonline.co.uk',
'http://www.thepoke.co.uk',
'http://www.birminghammail.co.uk',
'http://www.belfasttelegraph.co.uk',
'http://www.thedailymash.co.uk',
'http://www.theweek.co.uk',
'http://www.thescottishsun.co.uk',
'http://www.theargus.co.uk',
'http://www.news.co.uk',
'http://www.eveningtimes.co.uk',
'http://www.yorkpress.co.uk',
'http://www.thenorthernecho.co.uk',
'http://www.theboltonnews.co.uk',
'http://www.portsmouth.co.uk',
'http://www.grimsbytelegraph.co.uk',
'http://www.Politics.co.uk',
'http://www.investortimes.co.uk',
'http://www.belfastlive.co.uk',
'http://www.online.co.uk',
'http://www.news.co.uk', 
'http://www.thescarboroughnews.co.uk',
'http://www.deadlinenews.co.uk',
'http://www.larnetimes.co.uk',
'http://www.colerainetimes.co.uk',
'http://www.scottishfield.co.uk',
'http://www.dailyecho.co.uk']


def tokenized_Tagged(string):
    text = nltk.sent_tokenize(string)
    taggedText=nltk.pos_tag(text)
    return taggedText

# x = requests.get("http://www.bbc.com/news/politics")
# soup = BeautifulSoup(x.content, "html5lib")
# soup_text = soup.get_text()
# tokens = tokenized_Tagged(soup_text)#nltk.word_tokenize(soup_text)

soup_text =''
count = 0
for site in Target_Sites:
    count += 1
    print("Requesting site: ",site," ~~ [",count,"th / ",len(Target_Sites),"] ...")
    try:
        x = requests.get(site)
    except requests.exceptions.RequestException as ex:
        pass
    print("making soup [",count,"] ...")
    soup = BeautifulSoup(x.content, "html5lib")
    soup_text +=  soup.get_text() 
    print("tokenizing [",count,"] ...")
    tokens = tokenized_Tagged(soup_text)#nltk.word_tokenize(soup_text)


# print(re.search("no\s?deal",soup_text,re.IGNORECASE))
no_deal_list = [' '.join( item[0].split() ) for item in tokens if re.search(r"no\s?deal",item[0],re.IGNORECASE) ]
referendum_list = [' '.join( item[0].split() ) for item in tokens if re.search(r"second\s?referendum",item[0],re.IGNORECASE) ]
for listItem in no_deal_list:
    print( listItem +'\n')
for listItem in referendum_list:
    print( listItem +'\n')
print( "Total senteces containing \" no deal \": " , len(no_deal_list) )
print( "Total senteces containing \" second referendum \": " , len(referendum_list) )
# print(  )