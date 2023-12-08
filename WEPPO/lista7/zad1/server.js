var http = require('http');
var server =
    http.createServer(
    (req, res) => {
        if (req.method == 'POST') {
            console.log('POST')
            var body = ''
            // zbieranie danych z POST
            req.on('data', function(data) {
              body += data
              console.log('Partial body: ' + body)
            })
            // wysłanie odpowiedzi jak POST się skończy
            req.on('end', function() {
              console.log('Body: ' + body)
              res.writeHead(200, {'Content-Type': 'text/html'})
              res.end('post received')
            })
          }else {
            res.end(`hello world ${new Date()}`);
          }
    
});
server.listen(3000);
console.log('started');

/*
w burp
- wchodzimy do proxy, otwieramy przeglądarkę dajemy tam naszą stronę
- przeglądamy http history, klikamy prawym przyciskiem myszy i 'sent to repeater'
- zamieniamy GET na POST i vice versa i mamy już obie akcje do serwerów
*/