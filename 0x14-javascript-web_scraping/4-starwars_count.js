#!/usr/bin/node

const req = require('request');
req(process.argv[2], function (error, response, body) {
  if (!error) {
    let cont = 0;
    for (let i = 0; i < JSON.parse(body).results.length; i++) {
      for (let j = 0; j < JSON.parse(body).results[i].characters.length; j++) {
        if (JSON.parse(body).results[i].characters[j].includes('18')) {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
