#!/usr/bin/node

const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const myDict = {};
    for (const i in JSON.parse(body)) {
      if (JSON.parse(body)[i].completed === true) {
        if (myDict[JSON.parse(body)[i].userId] === undefined) {
          myDict[JSON.parse(body)[i].userId] = 1;
        } else {
          myDict[JSON.parse(body)[i].userId]++;
        }
      }
    }
    console.log(myDict);
  }
});
