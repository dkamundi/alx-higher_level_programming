#!/usr/bin/node


const fs = require('fs');

function readFileContent(filePath) {
	fs.readFile(filePath, 'utf-8', (err, data) => {
		if (err) {
			console.error(err);
		} else {
			console.log(data);
		}
	});
}
const filePath = process.argv[2];

if (!filePath) {
	console.error('Usage: node read-file.js <file-path>');
} else {
	readFileContent(filePath);
}
