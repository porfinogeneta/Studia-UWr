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

    // Retrieve all documents from the authors collection
    const authors = await collection.find({}).toArray();

    // Display the authors
    console.log('Authors Collection:');
    authors.forEach(author => {
      console.log(`ID: ${author._id}, Name: ${author.name}`);
    });

  } finally {
    // Close the MongoDB client
    await client.close();
  }
}

// Run the application
run().catch(console.error);
