/**
 *
 * @authors jiong (447991103@qq.com)
 * @date    2015-11-16 10:43:19
 * @version $Id$
 */

var system=require('system')
if(system.args.length===1)
{
	console.log('try to pass some args when invoking this script!');

}
else
{
	system.args.forEach(function(arg,i)
	{
		console.log(i+':'+arg);
	})
}
phantom.exit();