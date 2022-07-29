const express = require('express');
const app = express();
const defaultRoute = require("./routes/default");
var server = require('http').createServer(app);
var io = require('socket.io')(server);

//routes
app.use(defaultRoute);

app.use(express.static("public"));

server.listen(3000, "0.0.0.0", function() { 
	console.log('Server Has Started!'); 
});