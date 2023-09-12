#!/usr/bin/node
/* A class Square that defines a square and inherits from 4-rectangle.js */

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  // A Square class inherited from Rectangle class
  constructor (size) {
    super(size, size); // Calling Rectangle class constructor
  }
}

module.exports = Square;
