const express = require('express');
const csrf = require('csurf');
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');

// https://www.geeksforgeeks.org/implementing-csurf-middleware-in-node-js/
// https://github.com/Learn-by-doing/csrf-examples

let csrfProtection = csrf({ cookie: true });
let parseForm = bodyParser.urlencoded({ extended: false });

let app = express();
app.set('view engine', 'ejs');
const path = require('path')
app.set('views', path.join(__dirname, 'views'));

app.use(cookieParser());

// secure
app.get('/form', csrfProtection, function (req, res) {
    res.render('login', { csrfToken: req.csrfToken() });
});

// // not secure
// app.get('/form', function (req, res) {
//     res.render('login')
// });

app.post('/process', parseForm,
// not secure
//  function(req, res) {
//     res.send('Successfully Validated!!')
// });
// secured
	csrfProtection, function (req, res) {
		res.send('Successfully Validated!!');
	});

app.listen(4000, (err) => {
	if (err) console.log(err);
	console.log('Server Running');
});

// to wkleić od login.ejs
// <!-- <input type="hidden" name="_csrf"
//                value="<%= csrfToken %>"> -->

// --------------------------------------------
// ---------- Wroga aplikacja ----------
// --------------------------------------------



var evilApp = express();

evilApp.set('view engine', 'ejs');
evilApp.set('views', path.join(__dirname, 'views'));
evilApp.use(express.urlencoded({extended:true}));

evilApp.get("/", (req, res) => { 
    res.render("evilPanel")
});

evilApp.listen(4001, function() {
	console.log('Evil Server started and listening at localhost:4001');
});