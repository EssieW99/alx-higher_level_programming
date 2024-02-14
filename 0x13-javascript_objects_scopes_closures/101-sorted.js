#!/usr/bin/node
// a script that imports a dictionary of occurrences by user id and computes a dict of user ids by occurrence

// import dictionary
const dict = require('./101-data.js').dict;

// convert dict to an array of key-value pairs
const entries = Object.entries(dict);

// initialise a new object to store the new dictionary
const newDict = {};

// iterrate over each key-value pair
entries.forEach(([key, value]) => {
  // if no. of occurrences is not already a key, initialise it with an empty array
  if (!newDict[value]) {
    newDict[value] = [];
  }

  // push the  to the userId to the array corresponding to the no. of occurrences
  newDict[value].push(key);
});

// print new dictionary
console.log(newDict);
