// 8. Organize a complex HTTP server using Express
// 8.5 Write the server reusing everything you created

import express from 'express';

const routes = require('./routes/index');

const app = express();

app.use(routes);

app.listen(1245);

export default app;
