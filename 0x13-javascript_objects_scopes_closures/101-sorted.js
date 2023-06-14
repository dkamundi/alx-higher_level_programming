#!/usr/bin/node

const data = require('./101-data').dict;

const result = {};

for (const userId in data) {
	const occurences = data[userId];

	if (result[occurences]) {
		result[occurences].push(userId);
	} else {
		result[occurences] = [userId];
	}
}

console.log(result);
