#!/usr/bin/node
const argsCount = process.argv.length - 2;

if (argsCount === 0){
	console.log('No  Argument');
}else if (argsCount === 1){
	console.log('Aergument Found');
} else {
	console.log('Arguments Found');
}
