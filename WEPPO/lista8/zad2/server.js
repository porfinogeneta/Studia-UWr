var http = require('http');
var express = require('express');
var app = express();
const path = require('path')

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.use( (req, res) => {
    
    var przelewy = {
        name: 'przelewy1',
        options: [
        { kwota : 123, data : '2016-01-03', id : 1 },
        { kwota : 124, data : '2016-01-02', id : 2 },
        { kwota : 125, data : '2016-01-01', id : 3 }]
    };

    res.render('index', {przelewy});
});

http.createServer(app).listen(3000);