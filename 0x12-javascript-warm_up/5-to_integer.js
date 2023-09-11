#!/usr/bin/node
/* A script that prints My number: <first argument converted in integer> */

const firstArg = process.argv[2];

const num = parseInt(firstArg);

if (!isNaN(num)) {
  console.log('My number: ' + num);
} else {
  console.log('Not a number');
}
