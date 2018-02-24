from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

def isTwitterVerified(twitterUrl):
    url = re.search(".*twitter.com/([^/]*)", twitterUrl)[0]
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    profHeader = soup.find('span', attrs={'class':'ProfileHeaderCard-badges'})
    return profHeader is not None