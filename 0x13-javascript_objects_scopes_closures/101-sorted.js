#!/usr/bin/node

const dictionary = require('./101-data').dict;
const newd = {};
for (const key in dictionary) {
  newd[dictionary[key]] = [];
}
for (const key in dictionary) {
  newd[dictionary[key]].push(key);
}
console.log(newd);
