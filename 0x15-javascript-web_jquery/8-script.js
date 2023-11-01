// Strict mode to catch common coding errors and to improve security
'use strict';
/*
Fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
All movie titles must be list in the HTML tag UL#list_movies
*/
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
    data.results.forEach(function (movie) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
});
