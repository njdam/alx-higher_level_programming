#!/usr/bin/node
/* A script that prints x times “C is fun” */

const string = 'C is fun';

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('Missing number of occurrences');
} else {
  const max = process.argv[2];
  let i = 0;
  while (i < max) {
    console.log(string);
    i++;
  }
}
