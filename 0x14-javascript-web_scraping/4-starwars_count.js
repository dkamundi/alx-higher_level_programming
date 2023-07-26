#!/usr/bin/node
// script that should print the number of movies where the character "Wedge Antilles"
const request = require('request');

const apiUrl = process.argv[2];
const characterId = '18';

// Quering the api
request(apiUrl, function (error, response, body) {
	if (error) {
		// check for error
		console.error(error);
	} else {
		const films = JSON.parse(body).results;
		const numFilmsWithWedge = films.filter((film) => film.characters.includes('https://swapi-api.alx-tools.com/api/people/${characterId}/')).length;
		console.log(numFilmsWithWedge);
	}
});
