#!/usr/bin/node
const myVar = 'C is fun';
const coeficient = process.argv[2];

if (coeficient) {
  for (let i = 0; i < times; i++) console.log(myVar);
} else console.log('Missing number of occurrences');
