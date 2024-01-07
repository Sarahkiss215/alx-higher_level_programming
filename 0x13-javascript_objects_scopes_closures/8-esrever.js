#!/usr/bin/node

exports.esrever = function (list) {
  const nList = [];
  while (list.length) {
    nList.push(list.pop());
  }
  return nList;
};
