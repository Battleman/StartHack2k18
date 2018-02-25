from bs4 import BeautifulSoup
from urllib.request import urlopen

def getInfo(url) :
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    media = ''
    author = ''
    
    if ( 'foxnews.com' in url ) :
        media = 'foxnews'
        
        author = soup.find('div', attrs={'class':'author-byline'}).find('a').text.replace('\t', '').replace('\n', '')
        date = soup.find('time')['data-time-published']
        articleHTML = soup.find('div', attrs={'class':'article-body'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
    
    elif ('cnn.com' in url ) :
        media = 'cnn'
        
        author = soup.find('span', attrs={'class':'metadata__byline__author'}).find('a').text
        date = soup.find('meta', attrs={'itemprop':'dateCreated'})['content']
        articleHTML = soup.find('div', attrs={'itemprop':'articleBody'})
        
        #too random to be more clean
        article =articleHTML.text
        
        
        
    elif ('breitbart.com' in url ) :
        media = 'breitbart'
        
        author = soup.find('a', attrs={'class':'byauthor'}).text
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
        
        name = url.split('buzzfeed.com')[1].split('/')[1]
        author = soup.find('a', attrs={'href':'/'+name})['title']
        date = soup.find('time', attrs={'class':'buzz-timestamp__time js-timestamp__time'}).text
        articleHTML = soup.find('article')
        
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
        

            
    elif ('20min.ch' in url ) :
        #no always shown author
        media = '20min'
        
        title=soup.find('h3').find('span')
        if (title is not None) :
            author = title.text[4:]
        date = soup.find('div', attrs={'class':'published clearfix'}).find('span').text
        articleHTML = soup.find('div', attrs={'class':'story_text'})
        
        
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('24heures.ch' in url ) :
        media = '24heures'
        
        
        authorzone = soup.find('div', attrs={'class':'storyInfo'}).find('span', attrs={'class':'author'})
        if ( authorzone is not None) :
            author = authorzone.find('a').text[4:]
        
        date = soup.find('time', attrs={'class':'time'}).text
        articleHTML = soup.find('div', attrs={'id':'mainContent'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('letemps.ch' in url ) :
        media = 'letemps'
        
        authorzone = soup.find('span', attrs={'itemprop':'name'})
        if ( authorzone is not None) :
            author = authorzone.text
        
        date = soup.find('meta', attrs={'itemprop':'datePublished'}).text
        articleHTML = soup.find('div', attrs={'class':'body_content'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
            
    elif ('tdg.ch' in url ) :
        media = 'tdg'
        
        authorzone = soup.find('div', attrs={'class':'storyInfo'}).find('span', attrs={'class':'author'})
        if ( authorzone is not None) :
            author = authorzone.find('a').text[4:]
        
        date = soup.find('time', attrs={'class':'time'}).text
        articleHTML = soup.find('div', attrs={'id':'mainContent'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
    
    elif ('legorafi.fr' in url ) :
        media = 'legorafi'
        
        author = 'La Redaction'
        
        date = soup.find('span', attrs={'class':'context'}).text.split(' ')[2]
        articleHTML = soup.find('div', attrs={'class':'content'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('bbc.com' in url ) :
        media = 'bbc'
        
        authorzone = soup.find('span', attrs={'class':'byline__name'})
        if ( authorzone is not None) :
            author = authorzone.text[3:]
        
        date = soup.find('div', attrs={'class':'date date--v2'})['data-datetime']
        articleHTML = soup.find('div', attrs={'property':'articleBody'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
            
    elif ('nature.com' in url ) :
        media = 'nature'
        
        #author = soup.find('span', attrs={'class':'block hide-overflow nowrap overflow-ellipsis'}).text
        author = soup.find('h3', attrs={'id':'author-affiliation-news-0-head'}).text[21:-17]
        
        date = soup.find('time', attrs={'itemprop':'datePublished'}).text
        articleHTML = soup.find('div', attrs={'class':'article__body serif cleared'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
        
    elif ('washingtonpost.com' in url) :
        media = 'washingtonpost'
        
        authorzone = soup.find('span', attrs={'itemprop':'author'})
        if ( authorzone is not None) :
            author = []
            for a in authorzone.findAll('span', attrs={'itemprop':'name'}) :
                author.append(a.text)
        
        date = soup.find('span', attrs={'itemprop':'datePublished'}).text
        articleHTML = soup.find('article', attrs={'itemprop':'articleBody'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
    
    elif ('latimes.com' in url) :
        media = 'latimes'
        
        author = soup.find('a', attrs={'rel':'author'})['aria-label']
        date = soup.find('span', attrs={'class':'timestamp '}).text
        articleHTML = soup.find('section', attrs={'id':'left'})
        
        article = ''
        ps = articleHTML.findAll('p')
        for p in ps :
            article += p.text +'\n'
    
    
    
    
        
     
    hrefs = articleHTML.findAll('a')    
    sameHref = []
    diffHrefs = []
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
            sameHref += [newHref]
        else :
            diffHrefs += [newHref]
                    


        
    
    return {'author' :author ,'sameHref':sameHref,'diffHrefs':diffHrefs, 'domainRef' : domainRef , 'date':date,'article':str(article)}