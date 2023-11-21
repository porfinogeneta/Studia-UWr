const fs = require('fs')

// użyłem callback, ale jak byłoby więcej rzeczy do zrobienia jest mało praktyczny
fs.readFile('zad4/tekst.txt', 'utf-8', function(err, data) {
    console.log(data)
})