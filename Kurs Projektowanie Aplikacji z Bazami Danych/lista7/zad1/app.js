const { MongoClient } = require('mongodb');

// Connection URI for a local MongoDB server
const uri = 'mongodb://localhost:27017/library';

// Create a MongoDB client
const client = new MongoClient(uri);

async function run() {
  try {
    // Connect to the local MongoDB server
    await client.connect();
    console.log('Connected to the local database');

    // Specify the database and collection
    const database = client.db('library');
    const collection = database.collection('authors');


    // Clear the authors collection
    await collection.deleteMany({});
    console.log('Authors collection cleared');

    // Add records to the collection
    await collection.insertMany([
      { _id: 1, name: 'Golden' },
      { _id: 2, name: 'Golding' },
      { _id: 3, name: 'Bułhakow' },
    ]);

    console.log('Records added to the authors collection');

  } finally {
    // Close the MongoDB client
    await client.close();
  }
}

// Run the application
run().catch(console.error);
