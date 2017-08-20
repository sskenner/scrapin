from bs4 import BeautifulSoup, SoupStrainer
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import html2text

req = Request('https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743', headers={'User-Agent': 'Mozilla/5.0'})
# req = Request('https://jobs.lever.co/roam/ca9b536d-592b-4755-b03a-14df06274743', headers={'User-Agent': 'Mozilla/5.0'})
r = urllib.request.urlopen(req).read()

only_tag_class = SoupStrainer("div", {"class" : "section-wrapper page-full-width"})


soup = BeautifulSoup(r, "html.parser", parse_only=only_tag_class).prettify()

htmlText = soup.encode('utf-8').decode('utf-8', 'ignore')

print(html2text.html2text(htmlText))

