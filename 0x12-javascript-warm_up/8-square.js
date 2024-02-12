#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);

// check if the first arg can't be coverted to an int
if (isNaN(firstArg)) {
  console.log('Missing size');
}

// print square
let i = 0;
let j = 0;
for (i = 0; i < firstArg; i++) {
  let row = '';
  for (j = 0; j < firstArg; j++) {
    row += 'x';
  }
  console.log(row);
}
