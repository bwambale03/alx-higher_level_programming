class Rectangle {
  constructor (w, h) {
    if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
      this.width = w;
      this.height = h;
    } else {
      return {}; // Create an empty object if w or h is invalid
    }
  }
}
module.exports = Rectangle;
