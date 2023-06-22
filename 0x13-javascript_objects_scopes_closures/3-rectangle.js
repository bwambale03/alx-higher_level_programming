#!/usr/bin/node
module.exports = class Rectangle {
	constructor (w, h) {

		if (Number.isInteger(w) && w > 0 && Number.isInteger(h) && h > 0) {
			this.width = w;
			this.height = h;

			object = {
				// empty object
			}
	}
		print() {
			if (this.width === 0 || this.height === 0) {
				console.log('Empty Reactangle');
			} else {
				for (let i = 0; i < this.length; i++) {
					console.log('X'.repeat(this.width));
				}
			}
		}
};
