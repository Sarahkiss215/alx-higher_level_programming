#!/usr/bin/node

let Logs = 0;

exports.logMe = function (item) {
  console.log(`${Logs}: ${item}`);
  Logs++;
};
