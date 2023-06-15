#!/usr/bin/node

exports.callMeMoby = function(x, theFunction) {
	for (let i = 0; i < x; i++) theFunction();
};

function printFunction(){
	console.log("Executing theFunction");
}

exports.callMeMoby(3, printFunction);
