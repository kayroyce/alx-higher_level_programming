#!/usr/bin/node
/*
    prints all characters of a Star Wars movie in order
*/
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieId;

function kindPromise (characters, numChar) {
  if (numChar === characters.length) {
    return;
  }
  request(characters[numChar], function (errorC, responseC, bodyC) {
    if (errorC) {
      console.log('code:', responseC.statusCode);
    }
    console.log(JSON.parse(bodyC).name);
    kindPromise(characters, numChar + 1);
  });
}

request(url, function (error, response, body) {
  if (error) {
    console.log('code:', response.statusCode);
  } else {
    const jsonBody = JSON.parse(body);
    kindPromise(jsonBody.characters, 0);
  }
});
