var http = require('http');
const path = require('path')
const multer  = require('multer')
const upload = multer({ dest: 'zad1/uploads/' })

var express = require('express');
const { log } = require('console');

var app = express();
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));


app.get('/', (req, res) => {
    res.render('index.ejs')
})

app.post('/upload', upload.single('text_data'), (req, res, next) => {
    console.log(req.file);
    res.send('Upload has been successful!');
});

http.createServer(app).listen(3000);