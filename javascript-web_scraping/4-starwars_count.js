#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.hbtn.io/api/people/18/';
let counter = 0;
let i = 0;
let j = 0;

request(apiUrl, (error, response, body) => {
  if (error === null) {
    body = JSON.parse(body);
    const results = body.results;

    for (i in results) {
      for (j in results[i].characters) {
        if (results[i].characters[j] === characterUrl) {
          counter++;
        }
      }
    }

    console.log(counter);
  }
});
