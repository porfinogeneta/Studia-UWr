const http = require('https')

function fpromise(website){
    return new Promise((res, rej) => {
        http.get(website, function(resp) {
            let buf = ''
            
            resp.on('data', function(data) {
                buf += data.toString();
            });
            resp.on('end', function() {
                res(buf);
            });
            resp.on('error', function(err) {
                rej(err);
            });
        })
    })
}

fpromise('https://www.google.com')
    .then(result => console.log(result))
    .catch(err => console.log(err))
