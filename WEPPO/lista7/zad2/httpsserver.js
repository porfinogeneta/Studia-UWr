const https = require('https');
const fs = require('fs');

(async function () {
    var pfx = await fs.promises.readFile('domain.name.pfx');
    var server = https.createServer({
        pfx: pfx,
        passphrase: '1234'
    },
    (req, res) => {
        res.setHeader('Content-type', 'text/html; charset=utf-8');
        res.end(`hello world ${new Date()}`);
    });
    server.listen(3000);
    console.log('started');
})();



// openssl req -x509 -newkey rsa:4096 -keyout my_private_key.key -out my_cert.crt -sha256 -days 365
// openssl pkcs12 -export -out domain.name.pfx -inkey my_private_key.key -in my_cert.crt
//lsof -i :8002
//kill -9 <PID>


