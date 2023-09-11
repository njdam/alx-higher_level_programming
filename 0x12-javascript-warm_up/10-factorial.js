#!/usr/bin/node
/* A script that computes and prints a factorial */

function fact (n) {
  if (isNaN(n) || n <= 1) {
    return (1);
  } else {
    return (n * fact(n - 1));
  }
}

const num = parseInt(process.argv[2]);
const result = fact(num);
console.log(result);
