#!/usr/bin/node

const req = require('request');
req('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, body) {
  if (!error) {
    console.log(JSON.parse(body).title);
  }
});
