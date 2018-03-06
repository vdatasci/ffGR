from bs4 import BeautifulSoup as bs
import requests
import re

response = request.get('https://feedwm.org/faqs/click-here-for-our-mobile-food-pantry-schedule')
html = response.content
soup = bs(html, 'html.parser')

anchorContents = [link.string for link in soup.findAll('a')]
