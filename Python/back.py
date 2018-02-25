from bs4 import BeautifulSoup
from urllib.request import urlopen

def getInfo(url) :
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    media = ''
    
    if ( 'foxnews.com' in url ) :
        media = 'foxnews'
        
        date = soup.find('time')['data-time-published']
        articleHTML = soup.find('div', attrs={'class':'article-body'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
    
    elif ('cnn.com' in url ) :
        media = 'cnn'
        date = soup.find('meta', attrs={'itemprop':'dateCreated'})['content']
        articleHTML = soup.find('div', attrs={'itemprop':'articleBody'})
        
        #too random to be more clean
        article =articleHTML.text
        
        
        
    elif ('breitbart.com' in url ) :
        media = 'breitbart'
        date = soup.find('span', attrs={'class':'bydate'}).text
        articleHTML = soup.find('div', attrs={'class':'entry-content'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('buzzfeed.com' in url ) :
        
        for div in soup.find_all('div', attrs={'data-module':'action-bar-pagelevel'}): 
            div.decompose()
        
        soup.find('span', attrs={'class':'js-subbuzz__title-text'}).decompose()
        
        media = 'buzzfeed'
        date = soup.find('time', attrs={'class':'buzz-timestamp__time js-timestamp__time'}).text
        articleHTML = soup.find('article', attrs={'class':'buzz article article--long clearfix'})
        
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
        
     
    elif ('breitbart.com' in url ) :
        media = 'breitbart'
        date = soup.find('span', attrs={'class':'bydate'}).text
        articleHTML = soup.find('div', attrs={'class':'entry-content'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('20min.ch' in url ) :
        media = '20min'
        date = soup.find('div', attrs={'class':'published clearfix'}).find('span').text
        articleHTML = soup.find('div', attrs={'class':'story_text'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('24heures.ch' in url ) :
        media = '24heures'
        date = soup.find('time', attrs={'class':'time'}).text
        articleHTML = soup.find('div', attrs={'id':'mainContent'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('letemps.ch' in url ) :
        media = 'letemps'
        date = soup.find('meta', attrs={'itemprop':'datePublished'}).text
        articleHTML = soup.find('div', attrs={'class':'body_content'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
            
    elif ('tdg.ch' in url ) :
        media = 'tdg'
        date = soup.find('time', attrs={'class':'time'}).text
        articleHTML = soup.find('div', attrs={'id':'mainContent'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
    
    elif ('legorafi.fr' in url ) :
        media = 'legorafi'
        date = soup.find('span', attrs={'class':'context'}).text.split(' ')[2]
        articleHTML = soup.find('div', attrs={'class':'content'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
        
     
    hrefs = articleHTML.findAll('a')    
    sameHref = set()
    diffHrefs = set()
    domainRef=set()
    
    
        
    for h in hrefs :
        newHref = h.get('href')
        if newHref == None or len( newHref.split('/') )== 1 :
            continue
            
        if 'http' in newHref :
            domainRef.add(newHref.split('/')[2])
        else :
            domainRef.add(newHref.split('/')[0])
            
        if media in  newHref :
            sameHref.add(newHref)
        else :
            diffHrefs.add(newHref)
                    
    
    return {'sameHref':list(sameHref),'diffHrefs':list(diffHrefs), 'domainRef' : list(domainRef) , 'date':date,'article':str(article)}