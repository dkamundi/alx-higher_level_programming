#!/usr/bin/node

/* a script that prints the title of a Star Wars movie where
 the episode number matches a given integer.
*/
const request = require('request');
const episodeNum = process.argv[2];
const movieUrl = 'https://swapi-api.alx-tools.com/api/films/' + episodeNum;

request(movieUrl, function (error, response, body) {
	// checks for error
	if (error) {
		console.log(error);
	} else {
		const data = JSON.parse(body);
		console.log(data.title);
	}
});
