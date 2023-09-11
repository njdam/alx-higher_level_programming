#!/usr/bin/node
/* A script that prints the addition of 2 integers. */

function add (a, b) {
  return (a + b);
}

const args = process.argv.slice(2);

if (args.length < 2) {
  console.log('NaN');
} else {
  const a = parseInt(process.argv[2]);
  const b = parseInt(process.argv[3]);
  console.log(add(a, b));
}
