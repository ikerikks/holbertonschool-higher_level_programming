#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error === null) {
    let i = 0;
    const todosTab = {};

    body = JSON.parse(body);

    for (i in body) {
      if (body[i].completed === true) {
        if (todosTab[body[i].userId] === undefined) {
          todosTab[body[i].userId] = 0;
        }
        todosTab[body[i].userId]++;
        
      }
    }

    console.log(todosTab);
  }
});
