#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (error, body) {
  if (!error) {
    fs.writeFileSync(process.argv[3], body, 'utf-8');
  }
});
