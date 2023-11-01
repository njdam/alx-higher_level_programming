// Strict mode to catch common coding errors and to improve security
'use strict';
// A script to toggle header element to have one class: red or green
$(document).ready(function() {
  $('DIV#toggle_header').click(function() {
    $('header').toggleClass('red green');
  });
});
