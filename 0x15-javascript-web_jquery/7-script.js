// Strict mode to catch common coding errors and to improve security
'use strict';
/*
Fetches the character name from this URL: https://swapi-api.alx-tools.com/api/people/5/?format=json
The name must be displayed in the HTML tag DIV#character
*/
$(document).ready(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data) {
    $('DIV#character').text(data.name);
  });
});
