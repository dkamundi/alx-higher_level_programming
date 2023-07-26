#!/usr/bin/node

// script to compute the number of tasks completed by user id:

const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  // checking if there's error
  if (error) {
    console.error(error);
    return;
  }
  // pasing the JSON file
  const tasks = JSON.parse(body);
  const completedTasks = {};

  tasks.forEach(function (task) {
    if (task.completed) {
      if (completedTasks[task.userId]) {
        completedTasks[task.userId]++;
      } else {
        completedTasks[task.userId] = 1;
      }
    }
  });

  console.log(completedTasks);
});
