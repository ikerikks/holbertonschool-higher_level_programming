#!/usr/bin/node

const firstArg = Number(process.argv[2]);
let i = 0;
let j = 0;
let squareSymbol = '';

if (!firstArg) {
  console.log('Missing size');
} else {
  while (i < firstArg) {
    while (j < firstArg) {
      squareSymbol += 'X';
      j++;
    }

    console.log(squareSymbol);
    i++;
  }
}
