#!/usr/bin/node
/* A javascript to read and print the content of a file */

const fs = require('fs');
const filePath = process.argv[2];

// To check if file path is exists or not
if (!filePath) {
  console.log('Usage: ./read_file.js <file_path>');
  process.exit(1);
}

// Read file to get and print error or data
fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
