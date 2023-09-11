#!/usr/bin/node
/* A script to print a message depending on number of arguments passed */

const args = process.argv.slice(2);

if (args.length === 0) {
  console.log('No argument');
} else if (args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
