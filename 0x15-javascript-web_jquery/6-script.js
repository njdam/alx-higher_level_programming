// Strict mode to catch common coding errors and to improve security
'use strict';
// Update text of <header> element to New Header!!! when the user clicks on DIV#update_header
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('header').text('New Header!!!');
  });
});
