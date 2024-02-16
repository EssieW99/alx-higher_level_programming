#!/usr/bin/node
// a script that concats 2 files

// import fs module that provides functions for working with the file system
const fs = require('fs');

// get contents in first and second source file
const firstFile = fs.readFileSync(process.argv[2]).toString();
const secFile = fs.readFileSync(process.argv[3]).toString();

// write contents into file three
fs.writeFileSync(process.argv[4], firstFile + secFile);
