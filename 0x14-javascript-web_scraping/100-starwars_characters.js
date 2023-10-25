#!/usr/bin/node
/* A script to print all characters of a Star Wars movie */

const request = require('request');
const movieId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api'

data_StarWar = request(f'{apiUrl}/people/{movieId}')

request(apiUrl, (error, response, body) => {
	if (!error && response.statusCode === 200) {
		console.log(body)
	} else {
		console.error('Error:', error);
	}
});
