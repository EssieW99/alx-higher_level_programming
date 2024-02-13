#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  // initialise an empty array
  const num = [];
  // parse through the arguments from index 2
  for (let i = 2; i < process.argv.length; i++) {
    num.push(Number(process.argv[i]));
  }

  // sort the numbers in the array in descending order
  num.sort((a, b) => b - a);

  const secNum = num[1];

  console.log(secNum);
}
