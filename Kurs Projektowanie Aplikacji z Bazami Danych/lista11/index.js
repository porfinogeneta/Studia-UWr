const http = require('http');
const express = require('express');
const ejs = require('ejs');
const { getOrdersFromCustomer, getSpecimensFromOrder, addOrder, deleteOrder, getProductsByIds, updateSpecimanWithId, deleteSpecimenWithId, addSpecimen, getAll } = require('./api');
const cors = require('cors');
const { log } = require('console');

const app = express();
app.use(cors())
app.set('views', './views');
app.set('view engine', 'ejs');

app.use(express.json())
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Something went wrong!');
  });

app.get('/', (req,res) => {
    res.render('home')
})

// customer orders retrieved by customer id
app.get('/orders/:id', async (req,res, next) => {
    try {
        const id = req.params.id
        const orders = await getOrdersFromCustomer(id)
        if (!orders) {
            res.status(404).send('Product not found');
        } else {
            res.render('orders.ejs', {data: orders})
        }
    } catch (err){
        next(err)
    } 
})

app.post('/orders/:id', async (req,res, next) => {
    try {
        const id = req.params.id
        const order = await addOrder(id, 0.0, 'waiting');
        res.sendStatus(201)
      } catch (error) {
        next(error);
      }
})

app.delete('/orders/:id/:orderId', async (req,res, next) => {
    try {
        const orderId = req.params.orderId
        await deleteOrder(orderId);
        res.sendStatus(201)
      } catch (error) {
        next(error);
      }
})

app.get('/orders/details/:orderId', async (req, res, next) => {
    try {
        const orderId = req.params.orderId
        const specimens = await getSpecimensFromOrder(orderId)
        const uniqueProductIdsArray = [...new Set(specimens.map(spec => spec.productId))];
        // const products = await getProductsByIds(uniqueProductIdsArray)
        const products = await getAll('products')
        res.render('orderDetails.ejs', {specimens: specimens, products: products})
    }catch (err) {
        next(err)
    }
})

app.post('/orders/details/api', async (req, res, next) => {
    try {
        const { specimenId, newQuantity } = req.body;
        await updateSpecimanWithId(specimenId, newQuantity)
        res.sendStatus(201)
    }catch (err) {
        next(err)
    }
})

app.delete('/orders/details/api/:specimenId', async (req, res, next) => {
    try {
        const specimenId = req.params.specimenId
        await deleteSpecimenWithId(specimenId)
        res.sendStatus(201)
    }catch (err){
        next(err)
    }
})

app.post('/orders/details/api/:orderId/:productId', async (req, res, next) => {
    try {
        
        const productId = req.params.productId
        const orderId = req.params.orderId
        await addSpecimen(productId, orderId)
        res.sendStatus(201)
    }catch (err) {

    }
})



const port = 3000
http.createServer(app).listen(port);
console.log( `server up and running on port: ${port}` );