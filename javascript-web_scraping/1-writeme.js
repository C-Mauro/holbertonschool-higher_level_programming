#!/usr/bin/node

const fs = require('fs');
// 'fs' is the native module from Node.js

fs.writeFile(process.argv[2], process.argv[3], '\n', 'utf8', function (error) {
    if (error) {
        console.log(error);
    }
});
