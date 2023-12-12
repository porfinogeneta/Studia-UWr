var http = require('http');
var express = require('express');
var session = require('express-session');
var app = express();
app.set('view engine', 'ejs');

const path = require('path')
app.set('views', path.join(__dirname, 'views'));
app.disable('etag');

app.use(session({resave:true, // czy zapisywać sesję, nawet jak nie była zmieniana, w każdym request
     saveUninitialized: true, // czy zapisać, jak sesja jest nowa ale nie zmodyfiowana
     secret: 'qewhiugriasgy' // logowanie się do pliku cookie sesji
    }));


app.post('/', (req, res) => {
    console.log(req.session);
    req.session.destroy((err) => {
        if (err) {
        console.error('Error destroying session:', err);
        }
        res.redirect('/');
    });
});

app.get('/clear-value', (req, res) => {
    if (req.session.hasOwnProperty('sessionValue')){
        delete req.session.sessionValue
    }
    res.redirect('/');
})

app.use("/", (req, res) => {

    var sessionValue;
    if (!req.session.sessionValue) {
        sessionValue = new Date().toString();
        req.session.sessionValue = sessionValue;
    } else {
        sessionValue = req.session.sessionValue;
    }
    var sessionViewsCounter;
    if (!req.session.sessionViewsCounter){
        var sessionViewsCounter = 1
        req.session.sessionViewsCounter = sessionViewsCounter
    }else {
        // dostajemy się do obiektu w sesji i go modyfikujemy
        req.session.sessionViewsCounter += 1
        sessionViewsCounter = req.session.sessionViewsCounter
    }

    res.render("index", { sessionValue: sessionValue, sessionViewsCounter } );

});



http.createServer(app).listen(3000);