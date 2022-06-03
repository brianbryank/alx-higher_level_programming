#!/usr/bin/node
exports.esrever = function (list) {
  const ls = [];
  for (let i = list.length - 1; i >= 0; i--) {
    ls.push(list[i]);
  }
  return ls;
};
