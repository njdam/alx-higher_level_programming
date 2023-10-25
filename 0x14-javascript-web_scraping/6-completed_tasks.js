#!/usr/bin/node
/* script that computes the number of tasks completed by user id. */

const request = require('request');
// Getting api url from commandline arguments
const apiUrl = process.argv[2];

// Function to compute numbers of completed tasks
function computeCompletedTasks (todos) {
  const completedTasksByUser = {};

  // For each to to compute number of tasks completed
  todos.forEach((todo) => {
    if (todo.completed) {
      const userId = todo.userId.toString();
      if (completedTasksByUser[userId]) {
        completedTasksByUser[userId]++;
      } else {
        completedTasksByUser[userId] = 1;
      }
    }
  });

  return completedTasksByUser;
}

// Requesting info from apiUrl
request(apiUrl, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completedTasks = computeCompletedTasks(todos);

    console.log(completedTasks);
  } else {
    console.error('Error:', error);
  }
});
