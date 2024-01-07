#!/usr/bin/node
const dict = require('./101-data').dict;

const totaList = Object.entries(dict);
const val = Object.values(dict);
const uniqVal = [...new Set(val)];
const dictNew = {};
for (const j in uniqVal) {
  const list = [];
  for (const k in totaList) {
    if (totaList[k][1] === uniqVal[j]) {
      list.unshift(totaList[k][0]);
    }
  }
  dictNew[uniqVal[j]] = list;
}
console.log(dictNew);
