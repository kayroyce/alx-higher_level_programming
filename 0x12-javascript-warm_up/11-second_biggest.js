#!/usr/bin/node

const secNum = process.argv;

if (secNum.length <= 3) {
  console.log(0);
} else {
  console.log(secNum.sort((x, y) => y - x).slice(3)[0]);
}
