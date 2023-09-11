#!/usr/bin/node
/* A script that prints a square. */

const args = process.argv.slice(2);
const num = parseInt(process.argv[2]);

if (args.length === 0 || isNaN(num)) {
  console.log('Missing size');
} else {
  let i = 0;
  while (i < num) {
    let j = 0;
    let row = '';
    while (j < num) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
