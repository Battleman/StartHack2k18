from bs4 import BeautifulSoup
from urllib.request import urlopen

def getInfo(url) :
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    
    if ( 'foxnews' in url ) :
        
        date = soup.find('time')['data-time-published']
        articleHTML = soup.find('div', attrs={'class':'article-body'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
        
    elif ('cnn' in url ) :
        date = soup.find('meta', attrs={'itemprop':'dateCreated'})['content']
        articleHTML = soup.find('div', attrs={'itemprop':'articleBody'})
        
        article =articleHTML.text
     
    hrefs = articleHTML.findAll('a')    
    sameHref = []
    diffHrefs = []
    domainRef=set()
    
    for h in hrefs :
        newHref = h.get('href')
        if newHref == None :
            continue
        if 'http' in newHref :
            domainRef.add(newHref.split('/')[2])
        else :
            domainRef.add(newHref.split('/')[0])
            
        if 'foxnews' in  newHref :
            sameHref += [newHref]
        else :
            diffHrefs += [newHref]
    
    return {'sameHref':sameHref,'diffHrefs':diffHrefs, 'domainRef' : domainRef , 'date':date,'article':str(article)}