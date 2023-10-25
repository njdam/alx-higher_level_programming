#!/usr/bin/node
/* A javascript to print all characters of a Star Wars movie. */

const request = require('request');
const movieId = process.argv[2];
const movieUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

if (process.argv.length > 2) {
  request(movieUrl, (error, response, body) => {
    if (error) {
      console.error(error);
    }
    const charactersUrl = JSON.parse(body).characters;
    const charactersName = charactersUrl.map(
      url => new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          }
          resolve(JSON.parse(body).name);
        });
      }));
    Promise.all(charactersName)
      .then(names => console.log(names.join('\n')))
      .catch(error => console.error(error));
  });
}
