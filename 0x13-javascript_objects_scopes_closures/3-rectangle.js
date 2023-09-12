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

  print () {
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Rectangle;
