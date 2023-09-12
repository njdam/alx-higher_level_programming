#!/usr/bin/node
/* A script by adding a new function incr to increment integer value. */

const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);

// Addition of function in myObject to increment myObject value
myObject.incr = function () {
  myObject.value++; // Or this.value++;
};

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
