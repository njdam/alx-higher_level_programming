#!/usr/bin/node
/* A class Square that defines a square and inherits from 5-square.js */

const SquareParent = require('./5-square');

class Square extends SquareParent {
  // A Square class inherited from Parent Square class

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}

module.exports = Square;
