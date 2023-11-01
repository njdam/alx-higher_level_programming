// Strict mode to catch common coding errors and to improve security
'use strict';
// Adds a <li> element to a list when the user clicks on the tag DIV#add_item
$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
