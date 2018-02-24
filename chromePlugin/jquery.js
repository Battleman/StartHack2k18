var links = document.getElementsByTagName('a');

domain = document.URL.split("/")[2];

var hrefsSame = [] , hrefs = [] ;

for(var i = 0; i< links.length; i++){
	currHref = links[i].href;
	if (  links[i].href) {
		if(currHref.indexOf("http") !=-1 ) {
		//href += links[i].href;
			if(currHref.indexOf(domain) !=-1 ) {
				hrefsSame += currHref ;
			} else {
				hrefs += currHref ;
			};
		}
		
	}
 	
};
alert ("same : "+ String(hrefsSame.length) + "\n"+String(hrefsSame) + "\n\n" );
alert("diff : "+ String(hrefs.length)  + "\n"+String(hrefs));