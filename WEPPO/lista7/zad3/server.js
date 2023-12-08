const express = require('express');
const path = require('path')

const app = express()
const port = 8000

// umożliwia przekazywanie danych z <form>
app.use(express.urlencoded({ extended: true }));

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'))
})


app.post('/print', function (req, res) {
    console.log(res.body);
    const {imie, nazwisko, przedmiot, cells} = req.body;
    
    if (!imie || !nazwisko || !przedmiot) {
        res.status(400).sendFile(path.join(__dirname, 'index.html'));
        return;
      }
    res.redirect(`/print?imie=${imie}&nazwisko=${nazwisko}&przedmiot=${przedmiot}&cells=${cells}`)
  });

app.get('/print', (req,res) => {
    const {imie, nazwisko, przedmiot, cells} = req.query;
    const cellsParsed = JSON.parse(cells);
    console.log(cellsParsed);
    res.send(`
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Print Page</title>
        </head>
        <body>
            <h1>Print Page</h1>
            <p>Imię: ${imie}</p>
            <p>Nazwisko: ${nazwisko}</p>
            <p>Przedmiot: ${przedmiot}</p>
            <table>
            <thead>
                <tr>
                    <th>1</th>
                    <th>2</th>
                    <th>3</th>
                    <th>4</th>
                    <th>5</th>
                    <th>6</th>
                    <th>7</th>
                    <th>8</th>
                    <th>9</th>
                    <th>10</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>${cellsParsed[0]}</td>
                    <td>${cellsParsed[1]}</td>
                    <td>${cellsParsed[2]}</td>
                    <td>${cellsParsed[3]}</td>
                    <td>${cellsParsed[4]}</td>
                    <td>${cellsParsed[5]}</td>
                    <td>${cellsParsed[6]}</td>
                    <td>${cellsParsed[7]}</td>
                    <td>${cellsParsed[8]}</td>
                    <td>${cellsParsed[9]}</td>
                </tr>
            </tbody>
        </body>
        </html>
  `);

})

app.listen(port, () => {
    console.log(`App is running on port: ${port}`);
})
