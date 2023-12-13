#!/usr/bin/node
const { argv } = require('process');

function factorial (Num) {
  if (Num === 0 || isNaN(Num)) return (1);
  return (Num * factorial(Num - 1));
}

console.log(factorial(parseInt(argv[2])));
