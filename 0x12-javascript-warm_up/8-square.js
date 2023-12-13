#!/usr/bin/node
const { argv } = require('process');

if (isNaN(argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(argv[2]);
  const charArray = [];
  for (let n = 0; n < size; n++) {
    charArray.push('X');
  }
  for (let m = 0; m < size; m++) {
    console.log(charArray.join(''));
  }
}
