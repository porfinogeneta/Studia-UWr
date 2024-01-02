const mysql = require('mysql2');

// create the connection to database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'Z3',
  port: '4001'
})


function addNewWorkPerson(work_name, person) {
    // jeśli wcześniejszy then nic nie zwrócił następny otrzymuje undyfined
    return new Promise((res,rej) => {
        connection.query('INSERT INTO MIEJSCE_PRACY (NAME) VALUES (?)',
        [work_name],
        (err, result, fields) => {
            if (err){
                rej(err)
            }else {
                res(result)
            }
        }
        )
    }).then((result) => {
        return new Promise((res,rej) => {
            connection.query(
                'INSERT INTO OSOBA (NAME, SURNAME, SALARY, WORK_ID) VALUES (?, ?, ?, ?)',
                [person.name, person.surname, person.salary, result.insertId],
                (err, r, f) => {
                    if (err) {
                        rej(err)
                    }else {
                        res(r)
                    }
                }
                
              )
        })
    })
  
  }


const p = {
    name: 'Henry',
    surname: 'Valery',
    salary: 12.30
}

addNewWorkPerson('The Office', p).then(res => console.log(res))