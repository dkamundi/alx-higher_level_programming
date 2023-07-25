#!/usr/bin/node

const fs = require('fs');

function writeFileContent(filePath, content) {
	fs.writeFile(filePath, content, 'utf-8', (err) => {
		if (err) {
			console.error(err);
		} else {
			console.log('Content has been written to ${filePath} successfully.');
		}
	});
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

if (!filePath || !contentToWrite) {
	console.error('Usage: node 1-writeme.js <file-path> <content-to-write>');
} else {
	writeFileContent(filePath, contentToWrite);
}
