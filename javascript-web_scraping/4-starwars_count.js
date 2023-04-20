#!/usr/bin/node

const request = require('request');
const id = 18;
// send GET request to API URL
request(process.argv[2], (error, response, body) => {
  if (!error) {
    const data = JSON.parse(body);
    const movies = data.results.filter(film =>
      film.characters.some(url => url.endsWith(`/${id}/`))
    );
    console.log(`${movies.length}`);
  }
});
