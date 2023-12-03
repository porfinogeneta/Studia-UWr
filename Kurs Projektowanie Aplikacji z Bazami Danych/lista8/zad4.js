var neo4j = require('neo4j-driver');

// database connection
(async () => {
  // URI examples: 'neo4j://localhost', 'neo4j+s://xxx.databases.neo4j.io'
  const URI = 'neo4j+s://0cf9e4e6.databases.neo4j.io'
  const USER = 'neo4j'
  const PASSWORD = 'mBbxO2vvT3xvUmz4_DSzX31LwRlqSyBrNw6mJ4wAtKM'
  let driver

  try {
    driver = neo4j.driver(URI, neo4j.auth.basic(USER, PASSWORD))
    const serverInfo = await driver.getServerInfo()
    console.log('Connection established')
    console.log(serverInfo)

    // query
    const { records, summary, keys } = await driver.executeQuery(
        'MATCH (n:Person) RETURN n LIMIT 25',
        )

    console.log(
        `>> The query ${summary.query.text} ` +
        `returned ${records.length} records ` +
        `in ${summary.resultAvailableAfter} ms.`
    )

    console.log('>> Results')
    const tableData = records.map(record => {
        return { id: record.get('n').elementId, name: record.get('n').properties.name };
    });
    console.table(tableData)

  } catch(err) {
    console.log(`Connection error\n${err}\nCause: ${err.cause}`)
  } finally {
    if (driver){
        driver.close()
    }
  }
})();

