#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const mainUrl = process.argv[2];
const storeFilePath = process.argv[3];

request(mainUrl, (error, response, body) => {
  if (error === null) {
    fs.writeFileSync(storeFilePath, body);
  }
});
