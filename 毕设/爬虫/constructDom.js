/**
 * 
 * @authors jiong (447991103@qq.com)
 * @date    2015-11-16 15:03:39
 * @version $Id$
 */
var page=require('webpage').create(),
system=require('system'),
address;

if(system.args.length===1){
	phantom.exit();
}else{
	address=system.args[1];
	page.open(address,function(status){
		if (status!=='success'){
			phantom.exit();

		}else{
			var sc=page.evaluate(function(){
				return document.body.innerHTML;

			});
			window.setTimeout(function()
			{
				console.log(sc);
				phantom.exit();
			});

		}
	});
};







