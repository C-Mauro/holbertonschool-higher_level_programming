#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    fs.writeFileSync(process.argv[3], body, 'utf8');
  }
});
