#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
// const file = require('./file_2');
const characterUrl = 'https://swapi-api.hbtn.io/api/people/18/';

request(apiUrl, (error, response, body) => {
  if (error === null) {
    let counter = 0;
    body = JSON.parse(body);
    const results = body.results;

    for (let i = 0; i < results.length; i++) {
      for (let j = 0; j < results[i].characters.length; j++) {
        if (results[i].characters[j] === characterUrl) {
          counter++;
        }
      }
    }

    console.log(counter);
  }
});
