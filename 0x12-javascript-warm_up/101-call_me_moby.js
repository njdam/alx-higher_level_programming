#!/usr/bin/node
/* A function that executes x times a function. */

exports.callMeMoby = function (x, theFunction) {
  const max = x;
  for (let i = 0; i < max; i++) {
    theFunction();
  }
};
