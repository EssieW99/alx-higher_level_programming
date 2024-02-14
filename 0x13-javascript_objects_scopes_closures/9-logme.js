#!/usr/bin/node
// a function that prints the number of args already printed and the new args value

let count = 0;
exports.logMe = function (item) {
  console.log(count + ' : ' + item);
  count++;
};
