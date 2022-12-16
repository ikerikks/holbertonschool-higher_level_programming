#!/usr/bin/node

const previousSquare = require('./5-square');

class Square extends previousSquare {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      let row = '';

      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          row += c;
        }
        console.log(row);
        row = '';
      }
    }
  }
}

module.exports = Square;
