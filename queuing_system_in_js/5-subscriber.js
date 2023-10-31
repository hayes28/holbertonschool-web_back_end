// 5. Node Redis client publisher and subscriber
import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err.message}`);
});

// Subscribe to the channel
client.subscribe('holberton school channel');

// When a message is received on the channel
client.on('message', (channel, message) => {
    if (channel === 'holberton school channel') {
        console.log(message);
    }

// If the message is 'KILL_SERVER', unsubscribe and quit
    if (message === 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
});
