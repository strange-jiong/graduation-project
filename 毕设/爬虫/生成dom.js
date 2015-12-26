/**
 * 
 * @authors jiong (447991103@qq.com)
 * @date    2015-12-02 11:25:28
 * @version $Id$
 */

var page = require(‘webpage’).create();
page.open("https://zh.airbnb.com/rooms/905492?s=AWCORD3P", function() {
	var text = page.evaluate(function () {
return document.body.innerHTML;
});
console.log(text);
phantom.exit();
});