#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let times = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      times += 1;
    }
  }
  return times;
};
