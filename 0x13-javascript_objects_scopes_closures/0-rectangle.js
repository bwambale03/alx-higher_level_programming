#!/usr/bin/env node
class Rectangle {
  constructor (width, length) {
    this.width = width;
    this.length = length;
  }

  getArea () {
    return this.width * this.length;
  }

  getPerimeter () {
    return 2 * (this.length + this.width);
  }
}
const rect = new Rectangle(4, 8);
console.log(rect.getArea());

console.log(rect.getPerimeter());
