#!/usr/bin/node
/*
    prints the number of movies where the
    character “Wedge Antilles” is present.
*/
const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    let count = 0;
    for (const film of jsonBody.results) {
      for (const character of film.characters) {
        if (character.endsWith('/18/')) { // ...people/18 is Wedge Antilles
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
