#!/usr/bin/node
/*
    takes in 3 strings and sends a search request to the Twitter API
*/
const request = require('request');
const base64 = require('base-64');
const utf8 = require('utf8');
const consumerKey = process.argv[2];
const consumerSecret = process.argv[3];
const base64Bearer = base64.encode(utf8.encode(consumerKey + ':' + consumerSecret));
const searchString = process.argv[4];
const optionsTwitter = {
  url: 'https://api.twitter.com/oauth2/token',
  headers: {
    Authorization: 'Basic ' + base64Bearer,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  body: 'grant_type=client_credentials'
};

request.post(optionsTwitter, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const jsonBody = JSON.parse(body);
  const accessToken = jsonBody.access_token;

  const optionSearch = {
    url: 'https://api.twitter.com/1.1/search/tweets.json',
    headers: { Authorization: 'Bearer ' + accessToken },
    qs: {
      q: searchString
    }
  };

  request(optionSearch, function (error, response, body) {
    if (error) {
      console.log('code:', response.statusCode);
    } else {
      const twitsSearched = JSON.parse(body);
      for (const [index, infoTwit] of twitsSearched.statuses.entries()) {
        console.log(`[${infoTwit.id}] ${infoTwit.text} by ${infoTwit.user.name}`);
        if (index >= 4) {
          break;
        }
      }
    }
  });
});
