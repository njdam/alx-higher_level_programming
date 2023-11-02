// Strict mode to catch common coding errors and to improve security
'use strict';
/*
Fetches and prints how to say “Hello” depending on the language
API service: https://www.fourtonfish.com/hellosalut/hello/
The language code will be the value entered in the tag INPUT#language_code (ex: es, fr, en etc.)
The translation must be fetched when the user clicks on INPUT#btn_translate or
presses ENTER when the focus is on INPUT#language_code
The translation of “Hello” must be displayed in the HTML tag DIV#hello
*/
$(document).ready(function () {
  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();
    const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

    $.get(apiUrl, function (data) {
      $('DIV#hello').html(data.hello);
    });
  }

  $('INPUT#btn_translate').click(fetchTranslation);

  $('INPUT#language_code').keypress(function (event) {
    if (event.key === 'Enter') {
      fetchTranslation();
    }
  });
});
