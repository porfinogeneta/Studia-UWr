const fs = require('fs')

// tradycyjny model
function standardRead(file, enc, callback) {
    fs.readFile(file, enc, function(err, data) {
        if (err){
            callback(err, null)
        }else {
            callback(null, data)
        }
    })
}

// standardRead('zad7/tadeusz.txt', 'utf-8', (err, data) => {
//     if (err){
//         console.log(`Encountered error ${err}`);
//     }else {
//         console.log(`Here is data: ${data}`);
//     }
// })

// model z Promise
function promiseRead(file, enc){
    return new Promise((res, rej) => {
        fs.readFile(file, enc, (err, data) => {
            if (err){
                rej(err)
            }else {
                res(data)
            }
        })
    })
}

// promiseRead('zad7/tadeusz.txt', 'utf-8')
//     .then(data => console.log(`Here is the data: ${data}`))
//     .catch(err => console.log(err))

// model z util.promisify
const util = require('util')

const promisified_standardRead = util.promisify(standardRead)

// promisified_standardRead('zad7/tadeusz.txt', 'utf-8')
//     .then(data => console.log(`Here is the data: ${data}`))
//     .catch(err => console.log(err))


// model z promises
function promisesRead(file, enc) {
    return fs.promises.readFile(file, enc)
}
// promisesRead('zad7/tadeusz.txt', 'utf-8')
//     .then(res => console.log(res))
//     .catch(err => console.log(err))

// // wywołania z async
(async function (){
    const dataa = await promiseRead('zad7/tadeusz.txt', 'utf-8')
    const datab = await promisified_standardRead('zad7/tadeusz.txt', 'utf-8')
    const datac = await promisesRead('zad7/tadeusz.txt', 'utf-8')

    console.log(dataa);
    console.log('=================================');
    console.log(datab);
    console.log('=================================');
    console.log(datac);
})()
