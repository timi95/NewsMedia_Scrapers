import re #RegularExpression Module
import requests
from bs4 import BeautifulSoup
import nltk

def tokenized_Tagged(string):
    text = nltk.sent_tokenize(string)
    taggedText=nltk.pos_tag(text)
    return taggedText

# ARRAY OF SITES

Target_Sites = [
"http://www.vanguardngr.com",
"http://www.punching.com",
"http://www.thisdaylive.com",
"http://www.thenatonlineng.com",
"http://www.tribune.com.ng",
"http://www.ngrguardiannews.com",
"http://www.saharareporters.com",
"http://www.leadership.ng",
"http://www.sunnewsonline.com",
"http://www.pmnewsnigeria.com",
"http://www.dailytrust.com.ng",
"http://www.premiumtimesng.com",
"http://www.234next.com",
"http://www.dailyindependentnig.com",
"http://www.dailypost.ng",
"http://www.dailytimes.com.ng",
"http://www.channelstv.com",
"http://www.nationalmirroronline.net",
"http://www.nairaland.com",
"http://www.business day online.com",
"http://www.my daily news watching.com",
"http://www.completesportsNigeria.com",
"http://www.nigeriaworld.com",
"http://www.theadvocatengr.com",
"http://www.Nigerian observer news.com",
"http://www.nigerianpilot.com",
"http://www.peoplesdaily-online.com",
"http://www.champions.com.ng",
"http://www.businessnews.com.ng",
"http://www.nationaldailyng.com",
"http://www.compass newspaper.com",
"http://www.the tide news online.com",
"http://www.theabujainquirer.com",
"http://www.abujavoice.com",
"http://www.dailypost-ng.com",
"http://www.weeklytrust.dailytrust.com",
"http://www.blueprint.ng",
"http://www.nationalaccordnewspaper.com",
"http://www.urhobotimes.com",
"http://www.sundaytrust.com.ng",
"http://www.africapunch.com",
"http://www.tell.ng",
"http://www.thetimesnigeria.com",
"http://www.imotrumpeta.com",
"http://www.nigeria24news.com",
"http://www.networkafrica.com",
"http://www.nigeriannews.com",
"http://www.triumphnews.ng",
"http://www.naij.com"
]
# tokens = []
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


print("Listing Osinbajo ...")
Osinbajo_list =  [' '.join( item[0].split() ) for item in tokens if re.search(r"Osinbajo",item[0],re.IGNORECASE) ]
print("Listing Buhari ...")
Buhari_list =  [' '.join( item[0].split() ) for item in tokens if re.search(r"Buhari",item[0],re.IGNORECASE) ]
print("Listing Atiku ...")
Atiku_list =  [' '.join( item[0].split() ) for item in tokens if re.search(r"Atiku",item[0],re.IGNORECASE) ]

print( "Total senteces containing \" Osinbajo \": " , len(Osinbajo_list) )    
print( "Total senteces containing \" Buhari \": " , len(Buhari_list) )   
print( "Total senteces containing \" Atiku \": " , len(Atiku_list) )            
