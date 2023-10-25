#!/usr/bin/node
/* A javascript that writes a string to a file. */

const request = require('request');

if (process.argv.length > 2) {
  request
    .get(process.argv[2])
    .on('response', response => {
      console.log(`code: ${response.statusCode}`);
    });
}
