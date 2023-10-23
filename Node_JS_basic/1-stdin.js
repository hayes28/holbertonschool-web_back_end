// Create a program named 1-stdin.js that will be executed through command line

// Import the readline module to read from the command line
const readline = require('readline');

// Create a readline interface to read from stdin and write to stdout
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

console.log('Welcome to Holberton School, what is your name?');

// Set up an event listener for the 'line' event on the readline interface
// This event is emitted whenever the user enters a new line of text
rl.on('line', (input) => {
  console.log(`Your name is: ${input}`);

  rl.close();
});

// Set up an event listener for the 'close' event on the readline interface
// This event is emitted when the readline interface is closed
rl.on('close', () => {
  console.log('This important software is now closing');
});
