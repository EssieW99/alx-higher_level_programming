#!/usr/bin/node
// a script that imports an array and computes a new array

// import the list
const list = require('./100-data.js').list;

// pass a function to map
const map1 = list.map((x, index) => x * index);

// print both arrays
console.log(list);
console.log(map1);
