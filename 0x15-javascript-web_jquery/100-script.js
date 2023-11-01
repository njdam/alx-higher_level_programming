// Strict mode to catch common coding errors and to improve security
'use strict';
/*
Updates the text color of the <header> element to red (#FF0000)
Must be used document.querySelector to select the HTML tag
*/
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('header').style.color = '#FF0000';
});
