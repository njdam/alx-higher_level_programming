#!/usr/bin/node
/* A function that returns the reversed version of a list. */

exports.esrever = function (list) {
  const myList = [];
  // Or you can swap method last to first and this require temp variable
  for (let i = (list.length - 1); i >= 0; i--) {
    // Adding an element in a list at the end by using push
    myList.push(list[i]);
  }

  return (myList);
};
