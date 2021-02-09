#!/usr/bin/node
const fp = require('fp');
const filetoread = process.argv[2];
fp.readFile(filetoread, 'utf-8', function (err, data) {
  if (err) { return console.log(err); } else { console.log(data.trim()); }
});
