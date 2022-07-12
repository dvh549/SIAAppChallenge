const express = require('express');
const app = express();
const defaultRoute = require("./routes/default");
var server = require('http').createServer(app);
var io = require('socket.io')(server);

//routes
app.use(defaultRoute);

server.listen(3000, "localhost", function() { 
	console.log('Server Has Started!'); 
});