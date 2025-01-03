#!/usr/bin/node

const request = require('request');

// Get the Movie ID from command line argument
const movieId = process.argv[2];

// Define the API URL
const url = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

// Send a GET request to fetch movie data
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
    return;
  }

  // Parse the response body (JSON format)
  const movieData = JSON.parse(body);

  // Check if the movie exists
  if (!movieData || !movieData.characters) {
    console.log('No characters found');
    return;
  }

  // Loop through the characters and print each one
  movieData.characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      if (error) {
        console.log(error);
        return;
      }

      // Parse the character data and print the character name
      const characterData = JSON.parse(body);
      console.log(characterData.name);
    });
  });
});
