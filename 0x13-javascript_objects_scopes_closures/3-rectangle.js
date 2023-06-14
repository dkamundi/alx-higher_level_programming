#!/usr/bin/node

// class defining a rectangle
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      			this.height = h;
    }
  }

  print () {
    if (Object.keys(this).length === 0) {
      // Print an empty rectangle if the object is empty
      console.log('Empty Rectangle');
      return;
    }
    for (let i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }
};
