var http = require('http');
var express = require('express');
var app = express();

const secret = 'this is a secret';

function createSignature(parameter){


    var crypto = require('crypto');
    // /* tajny klucz, znany tylko na serwerze */
    
    // /* parametr który zobaczy użytkownik */
    // var parameter = '1';
    // /* podpis który też zobaczy użytkownik */
    var hmac =
        crypto
            .createHmac('sha256', secret)
            .update(parameter)
            .digest('hex');

    // ef2419aa1cf930ca3c86d0eb06e3e6d40e7c75012c7215f7a986ff5f98ce741d           
    // console.log( hmac );
    return hmac
}

// // podpis dla tej faktury
// wantedSignature = createSignature('1')


app.set('view engine', 'ejs');
const path = require('path')
app.set('views', path.join(__dirname, 'views'));
app.use(express.urlencoded({extended:true}));

app.get("/", (req, res) => { res.end("default page")});

function validate(res, req, id, signature){
    // wyliczamy podpis dla danej nam faktury
    key = createSignature(id)
    // porównujemy z podanym przez użytkownika kluczem
    if (signature !== key){
        res.render('404.ejs', { url : req.url })
    }else {
        res.end(`dynamicznie generowana faktura:
        ${req.params.id}`)
    }
    

}
    
app.get("/faktura/:id/:signature",
    (req, res) => { 
        // wersja z zabezpieczeniami
        validate(res, req, req.params.id, req.params.signature)
        // wersja bez zabezpieczeń
        // res.end(`dynamicznie generowana faktura:
        //     ${req.params.id}`)
});
// ... wcześniej inne mapowania ścieżek
app.use((req,res,next) => {
    res.render('404.ejs', { url : req.url });
});

http.createServer(app).listen(3000);