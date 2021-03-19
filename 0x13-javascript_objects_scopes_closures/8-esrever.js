#!/usr/bin/node

exports.esrever = function (list) {
  const inv = [];
  for (let i = list.length - 1; i >= 0; i--) {
    inv.push(list[i]);
  }
  return (inv);
};
