#!/usr/bin/node
exports.esrever = function (list) {
  const newLIst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newLIst.push(list[i]);
  }

  return newLIst;
};
