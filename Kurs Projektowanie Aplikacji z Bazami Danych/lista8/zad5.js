var neo4j = require('neo4j-driver');
require('dotenv').config();


class Realtionship{
    constructor (id, begin, end, name) {
        this.id = id,
        this.begin = begin
        this.end = end
        this.name = name
    }
}

class Person{
    constructor (id, properties) {
        this.id = id
        this.properties = properties
    }
}

class Movie{
    constructor (id, properties) {
        this.id = id
        this.properties = properties
    }
}

async function readNeo (driver) {
   
    // query
    const { records, summary, keys } = await driver.executeQuery(
        'Match (n)-[r]->(m) Return n,r,m'
    );

    console.log(
        `>> The query ${summary.query.text} ` +
        `returned ${records.length} records ` +
        `in ${summary.resultAvailableAfter} ms.`
    );


    console.log('>> Results');
    const persons = [];
    const movies = [];
    const relationships = [];
    records.forEach((record) => {
        if (persons.filter((e) => e.id == record.get('n').elementId).length == 0) {
            persons.push(new Person(record.get('n').elementId, record.get('n').properties));
        }
        if (movies.filter((e) => e.id == record.get('m').elementId).length == 0) {
            movies.push(new Movie(record.get('m').elementId, record.get('m').properties));
        }
        relationships.push(new Realtionship(record.get('m').elementId, record.get('n'), record.get('m'), record.get('r').type));
    });

    relationships.forEach(r => console.log(r));
    // movies.forEach((m) => console.log(m.properties));
    // // persons.forEach(p => console.log(p.properties))
    
    // return relationships,persons,movies
}

async function createNeo (driver, newData) {
    
    if (newData instanceof Person){
        // query
        await driver.executeQuery(
            `Create (:Person {name: ${newData.properties.name}})`
        );
    }else if (newData instanceof Movie){
        // query
        await driver.executeQuery(
            `Create (Movie {title: ${newData.properties.title}})`
        );
    }else if (newData instanceof Realtionship){
        // query
        await driver.executeQuery(
            `Create (m:Movie {title: ${newData.end.properties.title}}),
            (p:Person {name: ${newData.begin.properties.name}})
            (m)-[${newData.name}]->(p)`
        );
    }else {
        throw 'not valid object!'
    }
}
// data {id, property: 'prop name', new_val: 'new_val'} for example
async function updateNeo(driver, data){

    await driver.executeQuery(
        `Match (n) Where ID(n) = ${data.id} SET n.${data.property} = ${data.new_val}`
    );
}

// data = {id: id}
async function deleteNeo(driver, data){
    await driver.executeQuery(
        `Match (n) Where ID(n) = ${data.id} DELETE n`
    );
}
    




// database connection
async function functionCRUD(operation, data = null) {
    // URI examples: 'neo4j://localhost', 'neo4j+s://xxx.databases.neo4j.io'
    const URI = process.env.URI;
    const USER = 'neo4j';
    const PASSWORD = process.env.PASSWORD;
    let driver;

    

    try {
        driver = neo4j.driver(URI, neo4j.auth.basic(USER, PASSWORD));
        const serverInfo = await driver.getServerInfo();
        console.log('Connection established');
        console.log(serverInfo);

        
        if (operation == 'READ') {
            await readNeo(driver)
        }else if (operation == 'CREATE'){
            await createNeo(driver, data)
        }else if (operation == 'UPDATE'){
            await updateNeo(driver, data)
        }else if (operation == 'DELETE'){
            await deleteNeo(driver, data)
        }
        

    } catch (err) {
        console.log(`Connection error\n${err}\nCause: ${err.cause}`);
    } finally {
        if (driver) {
            driver.close();
        }
    }
}

