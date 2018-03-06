from bs4 import BeautifulSoup as bs
import requests
import re

response = request.get('https://feedwm.org/faqs/click-here-for-our-mobile-food-pantry-schedule')
html = response.content
soup = bs(html, 'html.parser')

anchorContents = [str(link.string) for link in soup.findAll('a')]

GRmatches = filter(re.compile('.*Grand Rapids.*').match, anchorContents)
indGRmatches = [i for i,val in enumerate(anchorContents) if re.match('.*Grand Rapids.*', val)]

[anchorContents[int(i) for i in indGRmatches]
