#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error === null) {
    let counter = 0;
    let i = 0;
    let j = 0;
    body = JSON.parse(body);
    const results = body.results;

    for (i in results) {
      for (j in results[i].characters) {
        if (results[i].characters[j].includes('18')) {
          counter++;
        }
      }
    }

    console.log(counter);
  }
});
