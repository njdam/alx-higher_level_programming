// Strict mode to catch common coding errors and to improve security
'use strict';
/*
Fetches from https://hellosalut.stefanbohacek.dev/?lang=fr and
displays the value of hello from that fetch in the HTML tag DIV#hello.
The translation of "hello" must be displayed in the HTML tag DIV#hello
*/
$(document).ready(function () {
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function (data) {
    $('DIV#hello').html(data.hello);
  });
});
