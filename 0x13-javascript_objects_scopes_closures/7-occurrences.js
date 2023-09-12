#!/usr/bin/node
/* A function that returns the number of occurrences in a list */

exports.nbOccurences = function (list, searchElement) {
  // Search Element and count it's occurences in a list
  let counts = 0;
  for (const element of list) { // or for (let i = 0; i < list.length; i++)
    if (element === searchElement) { // or if (list[i] === searchElement)
      counts++;
    }
  }

  return (counts);
};
