#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error === null) {
    let i = 0;
    let sum = 0;
    let counter = 1;
    const todosTab = {};
    let setValue = 0;

    // conversion of json data into js objects
    body = JSON.parse(body);
    // setting the control value for userId
    setValue = body[0].userId;

    for (i in body) {
      // check if the current userId is the same
      if (body[i].userId > setValue) {
        setValue = body[i].userId;
        // results.push(sum);
        todosTab[counter] = sum;
        sum = 0;
        counter++;
      }
      // computing number of task complete
      if (body[i].completed) {
        sum++;
      }
    }
    // adding number of task complete of last userId
    if (body[body.length - 1]) {
      todosTab[counter] = sum;
      counter++;
    }

    console.log(todosTab);
  }
});
