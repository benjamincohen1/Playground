var http = require("http")
var url= require("url")
function start(){
	http.createServer(function(request,response){
		var pathname = url.parse(request.url).pathname;
		console.log(pathname);
		response.writeHead(200,{"Content-Type": "text/plain"});
		response.write("Hello World")
		response.end();

	}).listen(8888)
}
exports.start = start;
start();
//codeeeeeeeeeeeee