const mysql = require('mysql2');

// create the connection to database
const connection = mysql.createConnection({
  host: 'localhost',
  user: 'root',
  database: 'Z2',
  port: '4001'
}).promise()

async function getPerson(){
    const [res]= await connection.query(
        'SELECT * FROM OSOBA'
      )
    return res
}


async function getOnePerson(id){
    const [res, fields] = await connection.query(
        'SELECT * FROM OSOBA WHERE OSOBA.ID = ?',[id]
      )
    console.log(fields);
}
// połączenie bez promise() wtedy z funkcji zwracamy Promise
// const connection = mysql.createConnection({
//     host: 'localhost',
//     user: 'root',
//     database: 'Z2',
//     port: '4001'
//   })

// function promisedBasedgetData(){
//     return new Promise((res, rej) => {
//         connection.query(
//             'SELECT * FROM OSOBA',
//             (err, result) => {
//                 if (err){
//                     rej(err)
//                 }else {
//                     res(result)
//                 }
//             }
//           )
//     })
// }

// promisedBasedgetData().then(result => {console.log(result)})



async function addPerson(name,surname,sex,age,salary) {
    const [res] = await connection.query(
        `INSERT INTO OSOBA (NAME, SURNAME, SEX, AGE, SALARY) VALUES(?, ?, ?, ?, ?)`,
        [name, surname,sex,age,salary],
    )
    return res;
}


async function updatePerson(col_name, new_val, id){
    await connection.query(
        `UPDATE OSOBA SET ${col_name} = ? WHERE OSOBA.ID = ?`,[new_val, id]
    )
    const result = await getOnePerson(id)
    return result;
}

async function deletePerson(id){
    return await connection.query(
        `DELETE FROM OSOBA WHERE ID = ?`,[id]
    )
}

// const res = addPerson("New", "User", "male", 10, 20.20)

(async () => {
    // const result = await getOnePerson(3)
    // console.log(result);
    // await getOnePerson(3)
    // const result = await getPerson()
    // console.log(result);
    // const id  = await addPerson("New", "User", "male", 10, 20.20)
    // console.log(id);
    // const result = await getPerson()
    // console.log(result);
    // const r = await updatePerson('NAME', 'Bartosz', 6)
    // console.log(r);
    // await deletePerson(5)
    // const result = await getPerson()
    // console.log(result);

})()

