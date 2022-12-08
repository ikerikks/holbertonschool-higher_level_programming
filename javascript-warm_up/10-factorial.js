#!/usr/bin/node

const firstArg = Number(process.argv[2]);

function factorial (n) {
  if (isNaN(n)) {
    console.log(1);
  } else {
    let i = n - 1;
    while (i > 0) {
      n *= i;
      i--;
    }
    console.log(n);
  }
}

factorial(firstArg);
