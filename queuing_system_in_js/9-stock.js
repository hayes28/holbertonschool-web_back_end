// 12. In stock?

import express from 'express';
import { createClient } from 'redis';
import { promisify } from 'util';

const app = express();
const client = createClient();

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const getItemById = id => listProducts.find(item => item.id === id);

const reserveStockById = async (itemId, stock) => {
    await client.setAsync(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async itemId => {
    const stock = await client.getAsync(`item.${itemId}`);
    return stock || null;
};

client.getAsync = promisify(client.get);
client.setAsync = promisify(client.set);

app.get('/list_products', (req, res) => {
    res.json(listProducts.map(({ id, name, price, stock }) => ({
        itemId: id,
        itemName: name,
        price,
        initialAvailableQuantity: stock
    })));
});

app.get('/list_products/:itemId', async (req, res) => {
    const product = getItemById(Number(req.params.itemId));
    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const currentStock = await getCurrentReservedStockById(product.id) || product.stock;
    res.json({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
        currentQuantity: Number(currentStock)
    });
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const product = getItemById(Number(req.params.itemId));
    if (!product) {
        return res.json({ status: 'Product not found' });
    }

    const currentStock = await getCurrentReservedStockById(product.id) || product.stock;
    if (currentStock <= 0) {
        return res.json({ status: 'Not enough stock available', itemId: product.id });
    }

    await reserveStockById(product.id, currentStock - 1);
    res.json({ status: 'Reservation confirmed', itemId: product.id });
});

app.listen(1245, () => console.log('Server is listening on port 1245'));
