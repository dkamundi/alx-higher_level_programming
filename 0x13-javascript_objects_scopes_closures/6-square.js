#!/usr/bin/node

// class defining a square
// inheriting from a rectangle

const square = require('./5-square');
module.exports = class Square extends square {

  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let squareString = '';

    for (let i = 0; i < this.width; i++) {
      squareString += c.repeat(this.width)+ '\n';
    }

    console.log(squareString);
  }
}
