var http = require('http');
var fs = require('fs');
http.createServer(function (req, res) {
    //Open a file on the server and return its content:
    fs.readFile('home.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data);
        res.end
    });
}).listen(8080);

http.createServer(function (req, res) {
    fs.readFile('human_migration.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data)
        return res.end();
    })
}).listen(8081);

http.createServer(function (req, res) {
    fs.readFile('human_migration.html', function (err, data) {
        res.writeHead(200, { 'Content-Type': 'text/html' });
        res.write(data)
        return res.end()
    });
}).listen(8082);


 
