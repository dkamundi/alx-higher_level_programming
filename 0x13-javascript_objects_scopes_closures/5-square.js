#!/usr/bin/node

// class defining a square
// inheriting from a rectangle

const Rectangle = require('./4-rectangle');
module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
