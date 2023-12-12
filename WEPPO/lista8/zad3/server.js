var http = require('http');
var express = require('express');
var app = express();

app.set('view engine', 'ejs');
const path = require('path')

app.set('views', path.join(__dirname, 'views'));

app.get('/download', (req, res) => {
    res.header('Content-disposition', 'attachment; filename="foo.txt"');
    res.header('Content-type', 'text/plain')
    res.end('tekst');
});

http.createServer(app).listen(3000);