#!/usr/bin/node

const length = process.argv.length;
const firstArg = process.argv[2];
let max = firstArg;
let secondMax = 0;
let i = 2;

while (i < length) {
  if (max < Number(process.argv[i])) {
    secondMax = max;
    max = Number(process.argv[i]);
  }

  if (Number(process.argv[i]) < max && Number(process.argv[i]) > secondMax) {
    secondMax = Number(process.argv[i]);
  }
  i++;
}

console.log(secondMax);
