const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const app = express();
const client = redis.createClient();

const getItemById = (id) => {
    return listProducts.find(product => product.id === id);
};

const reserveStockById = async (itemId, stock) => {
    const setAsync = promisify(client.set).bind(client);
    await setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
    const getAsync = promisify(client.get).bind(client);
    const reservedStock = await getAsync(`item.${itemId}`);
    return reservedStock ? parseInt(reservedStock) : 0;
};

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

app.get('/list_products', (req, res) => {
    res.json(listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    })));
});

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const currentQuantity = product.stock - await getCurrentReservedStockById(itemId);
    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: currentQuantity
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const itemId = parseInt(req.params.itemId);
    const product = getItemById(itemId);
    if (!product) {
        return res.json({ status: 'Product not found' });
    }
    const currentStock = product.stock - await getCurrentReservedStockById(itemId);
    if (currentStock <= 0) {
        return res.json({ status: 'Not enough stock available', itemId: itemId });
    }
    await reserveStockById(itemId, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId: itemId });
});

const PORT = 1245;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
