#!/usr/bin/node
/* A script to print all characters of a Star Wars movie */

const request = require('request');
const movieId = process.argv[2];

const movieURL = `https://swapi.dev/api/films/${movieId}/`;

request(movieURL, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode === 200) {
    const movieData = JSON.parse(body);
    const characters = movieData.characters;

    if (characters.length === 0) {
      console.log(`No characters found for movieId ${movieId}`);
    } else {
      characters.forEach((characterURL, index) => {
        request(characterURL, (charError, charResponse, charBody) => {
          if (charError) {
            console.error(`Error in fetching character ${index + 1}:`, charError);
          } else if (charResponse.statusCode === 200) {
            const characterData = JSON.parse(charBody);
            console.log(characterData.name);
          }
        });
      });
    }
  } else {
    console.error('Error: Movie not found.');
    process.exit(1);
  }
});
