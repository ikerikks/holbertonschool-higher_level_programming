#!/usr/bin/node

const firstArg = process.argv[2];

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  console.log('My number:', Math.floor(firstArg));
}
