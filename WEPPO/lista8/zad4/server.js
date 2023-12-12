var http = require('http');
var express = require('express');
var cookieParser = require('cookie-parser');
var app = express();
const path = require('path')

app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));
app.disable('etag');
app.use(cookieParser());
app.use(express.urlencoded({
    extended: true
}));

app.get("/", (req, res) => {
    var cookieValue;
    var another_cookieValue;
    // utworzenie ciastka, jak go nie ma
    if (!req.cookies.cookie) {
        cookieValue = new Date().toString();
        res.cookie('cookie', cookieValue);
    } else {
        // drukowanie wszystkich cookies
        // const cookiesss = req.headers.cookie 
        // console.log(cookiesss.split(', '));
        cookieValue = req.cookies.cookie;
    }
    // nie udało się znaleźć cookie, tzn że nie są włączone
    if (!req.cookies.cookie) {
        console.log('Cookies disabled!!');
    }
    
    if (!another_cookieValue){
        another_cookieValue = "I'am the other value"
        res.cookie('another_cookie', another_cookieValue)
    }else {
        another_cookieValue = req.cookies.another_cookieValue;
    }
    res.render("index", { cookieValue: cookieValue, another_cookieValue } );
});

app.post('/', (req, res) => {
    const all_cookies = (req.headers.cookie).split('; ')
    const cookies_ids = all_cookies.map(cookie => cookie.substring(0, cookie.indexOf("=")))
    // console.log(cookies_ids);
    // res.clearCookie('cookie')
    cookies_ids.forEach(cookie => res.clearCookie(cookie))
    res.end("Cookies deleted!")
})

http.createServer(app).listen(3000);