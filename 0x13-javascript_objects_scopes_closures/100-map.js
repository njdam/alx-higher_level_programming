#!/usr/bin/node
/* A script that imports an array and computes a new array. */

const list = require('./100-data').list;

// Printing Given list
console.log(list);
// Printing Modified list
console.log(
  list.map((x) => {
    return (x * (x - 1));
  })
);
