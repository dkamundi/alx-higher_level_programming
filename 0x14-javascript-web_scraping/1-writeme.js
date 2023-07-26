#!/usr/bin/node

// a script that writes a string to a file.

// Import error medule and assign variables
const fs = require('fs');
const filePath = process.argv[2];
const fileContent = process.argv[3];

// prints out the content of the file
fs.writeFile(filePath, fileContent, 'utf8', function (error) {
	// Checks for error
	if (error) {
		console.error(error);
	} else {
		console.log(fileContent);
	}
});
