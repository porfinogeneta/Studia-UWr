// mysql --socket /tmp/mysql_4002.sock -uroot

const mysql = require("mysql2")

const pool = mysql.createPool({
    host: '127.0.0.1',
    user: 'root',
    password: '',
    database: 'ecommerce',
    port: 4002
}).promise()

async function getAll(table){
    let rows = null
    switch (table){
        case('orders'):
            [rows] = await pool.query("SELECT * FROM orders")
            return rows
        case ('customers'):
            [rows] = await pool.query("SELECT * FROM customers")
            return rows
        default:
            [rows] = await pool.query("SELECT * FROM products")
            return rows
    }
        
    
}

async function getProduct(id){
    const [rows] = await pool.query("SELECT * FROM products WHERE id = ?", [id])
    return rows[0]
}

async function getProductsByIds(ids){
    try {
        const productsPromieses = ids.map(id => getProduct(id))
        const products = Promise.all(productsPromieses)
        return products
    }catch(err){
        throw err;
    }
}

async function getSpecimensFromOrder(orderId){
    const [rows] = await pool.query("SELECT * FROM specimens WHERE orderId = ?", [orderId])
    return rows
}

async function updateSpecimanWithId(id, newQuantity)
{
    const [result] = await pool.query(
        `UPDATE specimens SET quantity = ? WHERE id = ?`
    , [newQuantity, id]);
    return result
}

async function deleteSpecimenWithId(specimenId) {
    const [result] = await pool.query(`
        DELETE FROM specimens WHERE id = ?`, [specimenId])
    return result;
}

async function addSpecimen(productId, orderId){
    const [result] = await pool.query(`
    INSERT INTO specimens (productId, quantity, orderId)
    VALUES (?, 0, ?)
    `, [productId, orderId])
    const id = result.insertId;
    return id;
}

async function getOrdersFromCustomer(customerId){
    const [rows] = await pool.query("SELECT * FROM orders WHERE customerId = ?", [customerId])
    return rows
}

async function addOrder(customerId, total, purchase_status) {
    const [result] = await pool.query(`
    INSERT INTO orders (customerId, total, purchase_status)
    VALUES (?, ?, ?)
    `, [customerId, total, purchase_status])
    const id = result.insertId;
    return id;
}

async function deleteOrder(orderId) {
    const [result] = await pool.query(`
    DELETE FROM orders WHERE id = ?`, [orderId])
    return result;
}

async function getCustomer(){
    const [rows] = await pool.query("SELECT * FROM customers WHERE id = ?", [id])
    return rows[0]
}



async function addProduct(name, description, category, price, availability) {
    const [result] = await pool.query(`
    INSERT INTO products (name, description, category, price, availability)
    VALUES (?, ?, ?, ?, ?)
    `, [name, description, category, price, availability])
    const id = result.insertId;
    return getProduct(id);
}

async function deleteProduct(id){
    const [result] = await pool.query(
        `DELETE FROM products WHERE id = ?`
    , [id]);
    return result
}


async function updateProduct(col_name, new_val, id){

    const allowedColumns = ['description', 'name', 'price', 'availability', 'category']; 

    if (!allowedColumns.includes(col_name)) {
        throw new Error('Invalid column name');
    }

    const [result] = await pool.query(
        `UPDATE products SET ${col_name} = ?  WHERE id = ?`
    , [new_val, id]);
    return result
}


// (async () => {
//     // const res = await getAll('customers')
//     // const res = await getProduct(1)
//     // const res = await addProduct('product', 'amazing product', 'category', 20.20, 'available', 2)
//     // const res = await deleteProduct(4)
//     // const res = await updateProduct('name', 'New Name', 3)
//     const res = await getAll('products')
//     console.log(res);
// })()


module.exports = {
    getAll,
    getProduct,
    addProduct,
    deleteProduct,
    updateProduct,
    getOrdersFromCustomer,
    getSpecimensFromOrder,
    addOrder,
    deleteOrder,
    getProductsByIds,
    updateSpecimanWithId,
    deleteSpecimenWithId,
    addSpecimen
};

