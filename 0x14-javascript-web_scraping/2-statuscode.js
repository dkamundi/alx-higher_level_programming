#!/usr/bin/node

const request = require('request');
const url = process.argv[2]

request.get(url, function (error, response, body) {
	if (!error && response.statusCode === 200) {
		console.log('code:', response.statusCode);
	} else {
		console.log('code:', response.statusCode);
	}
});
