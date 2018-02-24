from bs4 import BeautifulSoup
from urllib.request import urlopen

def getInfo(url) :
	if("foxnews" not in url):
		return dict()
	html = urlopen(url)
	soup = BeautifulSoup(html, 'html.parser')

	date = soup.find('time')['data-time-published']
	articleHTML = soup.find('div', attrs={'class':'article-body'})


	domain = url.split('/')[2]


	hrefs = articleHTML.findAll('a')

	sameHref = []
	diffHrefs = []
	domainRef=set()
	for h in hrefs :
	    newHref = h['href']
	    domainRef.add(newHref.split('/')[2])
	    if 'http' in newHref :
	        
	        if 'foxnews' in  newHref :
	            sameHref += [newHref]
	        else :
	            diffHrefs += [newHref]


	article = ''
	ps = articleHTML.findAll('p')
	for p in ps :
	    article += p.text +'\n'
	return {'sameHref':sameHref,'diffHrefs':diffHrefs, 'domainRef' : domainRef , 'date':str(date),'article':str(article)}