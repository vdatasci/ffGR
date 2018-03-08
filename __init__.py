from bs4 import BeautifulSoup as bs
import requests
import re
from dateutil import parser
from datetime import datetime
import datetime


response = requests.get('https://feedwm.org/faqs/click-here-for-our-mobile-food-pantry-schedule')
html = response.content
soup = bs(html, 'html.parser')

#anchorContents = [str(link.string) for link in soup.findAll('a')]
#GRmatches = filter(re.compile('.*Grand Rapids.*').match, anchorContents)
#indGRmatches = [i for i,val in enumerate(anchorContents) if re.match('.*Grand Rapids.*', val)]
#[anchorContents[int(i) for i in indGRmatches]

#lis = [li.text for li in soup.findAll('li')]
#lis = [x.encode('utf-8').strip() for x in lis]

#grtimes = filter(re.compile('[0-9]:[0-9]').match, lis)

#filter(re.compile('[0-9]+..[0-9]').match, grtimes)

tags = [tag.text for tag in soup.findAll(['h3','li'])]
tags = [tag.encode('utf-8').strip() for tag in tags]
ffdata = filter(re.compile('[0-9]:[0-9]|\w+.\d+\,.\d+').match, tags)


for x in ffdata:
    if re.match('\w+.\d+\,.\d+', x) is not None:
        print(x)


## Example of datetime parser
#parser.parse('March 7, 2018 4:00 PM')


#h3s = [h3.text for h3 in soup.findAll('h3')]
#h3s = [h3.encode('utf-8').strip() for h3 in h3s]
#grdates = filter(re.compile('\w+.\d+\,.\d+').match, h3s)
#grdates = [parser.parse(str(d)).strftime('%Y-%m-%d') for d in grdates]


#2018-03-6T10:00:00+02:00



