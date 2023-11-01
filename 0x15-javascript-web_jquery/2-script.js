// Strict mode to catch common coding errors and to improve security
'use strict';
// A script to change header text color to red when clicked on
$(document).ready(function() {
  $('DIV#red_header').click(function() {
    $('header').css('color', '#FF0000')
  })
});
