#!/usr/bin/node
/* A script to print all characters of a Star Wars movie */

const request = require('request');
const movieUrl = 'https://swapi-api.hbtn.io/api';
const movieId = process.argv[2];

if (process.argv.length > 2) {
  request(`${movieUrl}/films/${movieId}/`, (error, response, body) => {
    if (error) {
      console.error('Error:', error);
    }
    const charactersUrl = JSON.parse(body).characters;
    charactersUrl.forEach(name => {
      request(name, (error, response, body) => {
        if (error) {
          console.error('Error:', error);
        }
        console.log(JSON.parse(body).name);
      });
    });
  });
}
