#!/usr/bin/node

const y = parseInt(process.argv[2]);

function Factorial (num) {
  if ((num === 1) || (Number.isNaN(num))) {
    return 1;
  }
  return Factorial(num - 1) * num;
}
console.log(Factorial(y));
