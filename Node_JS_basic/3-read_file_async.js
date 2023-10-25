// Reading a file asynchronously with Node JS

const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n');
    const header = lines.slice(1);  // Exclude the CSV header line

    let totalStudents = 0;
    const studentsByField = {};

    for (const student of header) {
      const fields = student.split(',');
      if (fields.length === 4) {
        const field = fields[3];
        totalStudents += 1;
        if (!studentsByField[field]) {
          studentsByField[field] = [];
        }
        studentsByField[field].push(fields[0]);
      }
    }

    // Construct the response text
    let responseText = `Number of students: ${totalStudents}\n`;
    for (const field in studentsByField) {
      if (Object.prototype.hasOwnProperty.call(studentsByField, field)) {
        const list = studentsByField[field];
        const count = list.length;
        const names = list.join(', ');
        responseText += `Number of students in ${field}: ${count}. List: ${names}\n`;
      }
    }

    return responseText;
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
