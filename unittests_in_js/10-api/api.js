// 10. Deep equality & Post integration testing
// Have to change port to 3000 from 7865
const express = require('express');
const app = express();
app.use(express.json());

app.get('/', function (req, res) {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id([0-9]+)', function (req, res) {
    res.send(`Payment methods for cart ${req.params.id}`);
});

app.get('/available_payments', function (req, res) {
    res.json({
        payment_methods: {
            credit_cards: true,
            paypal: false
        }
    });
});

app.post('/login', function (req, res) {
    const userName = req.body.userName;
    res.send(`Welcome ${userName}`);
});

app.listen(3000, () => {
    console.log('API available on localhost port 3000')
});
