#!/usr/bin/node
/* A script that prints two arguments passed to it,
 * in the following format: "is"
 */
console.log(process.argv[2] + ' is ' + process.argv[3]);

// const args = process.argv.slice(2);
// if (args.length === 0) {
//   console.log(process.argv[2] + ' is undefined');
// } else if (args.length === 1) {
//   console.log(process.argv[2] + ' is undefined');
// } else {
//   console.log(process.argv[2] + ' is ' + process.argv[3]);
// }
