#!/usr/bin/node
// A script to get the contents of a webpage and store it in a file:
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, function (error, response, body) {
  // checks if there's error
  if (error) {
    console.error(error);
    return;
  }

  fs.writeFile(filePath, body, 'utf-8', function (error) {
    if (error) {
      console.error(error);
    }
    // console.log(`Content of ${url} has been saved to ${filePath}`);
  });
});
