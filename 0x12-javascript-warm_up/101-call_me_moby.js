#!/usr/bin/node

function executeXtimes(x, theFunction) {
	for (let i = 0; i <= x; i++) {
		theFunction();
	}
}

function printMessage() {
	console.log('Executing theFunction');
}

executeXtimes(3, printMessage);
