#!/usr/bin/node
function factorial (n) {
  // check for NaN and the base case
  if (isNaN(n) || n === 0) {
    return (1);
  }

  // call the factorial function until the base case is reached
  return (n * factorial(n - 1));
}

// print the factorial of the first argument
console.log(factorial(Number(process.argv[2])));
