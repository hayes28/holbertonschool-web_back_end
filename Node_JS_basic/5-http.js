// 5. Create a more complex HTTP server using Node's HTTP module

const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer(async (req, res) => {
  res.setHeader('Content-Type', 'text/plain');
  if (req.url === '/') {
    res.write('Hello Holberton School!');
    res.end();
  } else if (req.url === '/students') {
    res.write('This is the list of our students\n');
    try {
      const studentsByField = await countStudents('./test/database.csv');
      res.write(studentsByField);
    } catch (error) {
      res.write('Cannot load the database\n');
    }
    res.end();
  } else {
    res.statusCode = 404;
    res.end();
  }
});
app.listen(1245);

module.exports = app;
