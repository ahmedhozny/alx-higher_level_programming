#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w ?? 0) < 1 || (h ?? 0) < 1) {
      return;
    }
    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
