#!/usr/bin/node
/* A class Rectangle that defines a rectangle */

class Rectangle {
  // A class Rectangle that defines a Rectangle with attributtes
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      // Create empty object if w or h is not a positive integer
      Object.create(null);
    }
  }

  // An instance method to print a rectangle
  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  // An instance method to exchanges the width with the height of rectangle
  rotate () {
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  // An instance method to double width and height
  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
