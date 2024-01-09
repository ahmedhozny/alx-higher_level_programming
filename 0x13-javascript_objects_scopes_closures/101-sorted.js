#!/usr/bin/node
const dict = require('./101-data.js').dict;

const allEntries = Object.entries(dict);
const vals = [...new Set(Object.values(dict))];
const newDict = {};
for (const val in vals) {
  const list = [];
  for (const key in allEntries) {
    if (allEntries[key][1] === vals[val]) {
      list.unshift(allEntries[key][0]);
    }
  }
  newDict[vals[val]] = list;
}

console.log(newDict);
