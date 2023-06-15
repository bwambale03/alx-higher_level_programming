#!/usr/bin/node
function executeXtimes(x, theFunction) {
	for (let i = 0; i <= x; i++) {
		theFunction();
	}
}
function Uganda() {
	console.log('Rich in Natural Resources');
}
executeXtimes(3, Uganda);
