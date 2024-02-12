#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);

// check if the first arg can't be coverted to an int
if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
}

// print x times
let x = 0;
while (x < firstArg) {
  console.log('C is fun');
  x++;
}
