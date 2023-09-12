#!/usr/bin/node
/* A function that converts a number from base 10
 * to another base passed as argument
 */

exports.converter = function (base) {
  return function (xNum) {
    // Converting a number in base 10 to another base
    return xNum.toString(base);
  };
};
