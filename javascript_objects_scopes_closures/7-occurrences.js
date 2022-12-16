#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;

  list.forEach((element) => {
    if (element === searchElement) {
      counter++;
    }
  });
  return counter;
};
