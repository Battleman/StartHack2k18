

//$("[data-vr-zone=zone-1-0]").css("background-color", "yellow");
var domain = document.URL.split("/")[2];


var article ;
var date;
var textArticle = "";



if (domain.indexOf("cnn") != -1 ){
	var dateContainer = document.querySelector("article").childNodes;
	date = dateContainer[2].getAttribute("content");



var articleList = document.querySelector("div[itemprop]").childNodes;

//alert(articleList.getAttribute("class"));
for(var i = 0; i< articleList.length; i++) {
	if (articleList[i].hasAttribute("data-vr-zone") && articleList[i].getAttribute("data-vr-zone") ==  "zone-1-0" ){
		alert("done");
		article = articleList[i]; 
		alert(articleList[i].getAttribute("data-vr-zone"));
	}
}
}else if(domain.indexOf("foxnews") != -1) {
	date = document.getElementsByTagName("time")[0].getAttribute("data-time-published");
	article = document.getElementsByClassName("article-body")[0];
	
	var articleP = article.getElementsByTagName("p");
	
	for(var i = 0; i< articleP.length; i++) {
		textArticle+= articleP[i].textContent + "\n";
	}
	
};

alert (textArticle);
article.style.border = "10px solid red";
alert (date);
var links = article.getElementsByTagName('a');




var hrefsSame = [] , hrefs = [] ;

for(var i = 0; i< links.length; i++){
	currHref = links[i].href;
	if (  links[i].href) {
		if(currHref.indexOf("http") !=-1 ) {
			if(currHref.indexOf(domain) !=-1 ) {
				hrefsSame.push(currHref );
			} else {
				hrefs.push( currHref );
			};
		}
		
	}
 	
};
alert ("same : "+ String(hrefsSame.length) + "\n"+String(hrefsSame) + "\n\n" );
alert("diff : "+ String(hrefs.length)  + "\n"+String(hrefs));