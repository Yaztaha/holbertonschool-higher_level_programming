#!/usr/bin/node
const myVar = 'X';
const coeficient = process.argv[2];

if (parseInt(coeficient)) {
  for (let i = 0; i < coeficient; i++) console.log(myVar.repeat(coeficient));
} else console.log('Missing size');
