#!/usr/bin/node

const firstArg = process.argv[2];
let x = 0;

if (!firstArg) {
  console.log('Missing number of occurrences');
} else {
  while (x < firstArg) {
    console.log('C is fun');
    x++;
  }
}
