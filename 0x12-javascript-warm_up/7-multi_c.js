#!/usr/bin/node

const y = process.argv[2];

if (isNaN(y)) {
	console.log('Missing number of occurrences');
}else {
 for (let i = 0; i < y; i++) {
	console.log('C is fun');
 }
}
