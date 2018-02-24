var i = 0;
var port = chrome.runtime.connect();
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
	  i=1;
   //alert(request);
	  console.log("ahahahahahahahhahahaha");
alert("non");
	  sendResponse({farewell: "goodbye"});
  });

if(i == 1){
	alert("non");
}