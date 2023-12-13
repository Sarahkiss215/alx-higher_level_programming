#!/usr/bin/node
const { argv } = require('process');

const argvLen = argv.length - 2;
if (argvLen <= 0) {
  console.log('No argument');
} else if (argvLen === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
