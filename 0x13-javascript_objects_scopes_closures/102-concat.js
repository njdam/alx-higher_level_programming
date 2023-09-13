#!/usr/bin/node
/* A script that concats 2 files. */

// Importing buildin file system `fs`
const fs = require('fs');

// Retrieving content of first and second arguments (files) to be concated
const Arg1 = fs.readFileSync(process.argv[2]).toString();
const Arg2 = fs.readFileSync(process.argv[3]).toString();

// Writing contents of concated files to third argument file
fs.writeFileSync(process.argv[4], Arg1 + Arg2);
