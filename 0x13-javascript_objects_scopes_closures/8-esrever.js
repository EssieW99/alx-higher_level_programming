#!/usr/bin/node
// function that returns the reversed version of a list

exports.esrever = function (list) {
  const l = [];
  for (let i = list.length - 1; i > 0; i--) {
    l.push(list[i]);
  }
  return (l);
};
