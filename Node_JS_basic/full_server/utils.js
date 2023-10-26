// 8. Organize a complex HTTP server using Express
// 8.1 Organize the structure of the server
// file create a function named readDatabase that accepts a file path as argument:

const fs = require('fs').promises;

async function readDatabase(filePath) {
  try {
    const data = await fs.readFile(filePath, 'utf8');
    const lines = data.trim().split('\n');
    const students = lines.slice(1);

    const studentsByField = {};

    students.forEach((studentLine) => {
      const [firstName, , , field] = studentLine.split(',');
      if (field) {
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(firstName);
      }
    });

    return Promise.resolve(studentsByField);
  } catch (error) {
    return Promise.reject(new Error('Cannot load the database'));
  }
}

export default readDatabase;
