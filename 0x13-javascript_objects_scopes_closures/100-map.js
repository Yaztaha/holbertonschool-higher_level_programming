#!/usr/bin/node
const a = require('./100-data').list;
console.log(a);
const aa = a.map((x, index) => x * index);
console.log(aa);
