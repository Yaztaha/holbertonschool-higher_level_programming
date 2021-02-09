#!/usr/bin/node

const req = require('request');
const fs = require('fs');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    fs.writeFile(process.argv[3], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
