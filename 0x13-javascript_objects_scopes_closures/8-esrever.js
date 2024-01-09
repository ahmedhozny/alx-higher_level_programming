#!/usr/bin/node
exports.esrever = function (list) {
  for (let i = 0, len = list.length - 1; i < len; i++, len--) {
    const temp = list[i];
    list[i] = list[len];
    list[len] = temp;
  }
  return list;
};
