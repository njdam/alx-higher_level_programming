#!/usr/bin/node
/**
 * A script that searches the second biggest integer
 * in the list of arguments.
 */

const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log('0');
} else {
  // Converting command-line args to an array of integers
  const array = process.argv.slice(2).map(Number);
  // sorting an array and chosing the number at index [1] second biggest num
  const secNum = array.sort(function (a, b) { return b - a; })[1];
  console.log(secNum);
}
