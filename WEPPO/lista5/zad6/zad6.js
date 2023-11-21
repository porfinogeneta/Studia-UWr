const fs = require('fs')
const readline = require('readline')

// tu będziemy przetrzymywać obiekty {key: ip, ilość_zapytań: Number}
const users = []

function fpromise (file){
    return new Promise((res, rej) => {

        const fileSystem = fs.createReadStream(file)

        const read = readline.createInterface({
            input: fileSystem,
            crlfDelay: Infinity
        })

        read.on('line', (line) => {
            const userIP = (line.split(' '))[1]
            let idx = users.findIndex((obj) => obj['key'] === userIP) // indeks do sprawdzania czy wartość była już w Array
            if (idx !== -1){
                users[idx].queryNum += 1
            }else {
                users.push({key: userIP, queryNum: 1})
            }
            // console.log(`Line: ${line}`);
        });
        
        read.on('close', () => {
            // jeżeli u1 - u2 < 0 => u1 będzie przed u2, mamy malejący porządek
            res((users.sort((u1, u2) => u2.queryNum - u1.queryNum)).slice(0,3))
            // console.log('Finished reading the file.');
        });

        read.on('error', (err) => {
            rej(err)
        })
    })
}

fpromise('zad6/logi.txt')
    .then(result => result.forEach(res => console.log(res.key)))

