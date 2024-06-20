#!/usr/bin/node
const value = Number(process.argv[2]);
function factorial (x) {
  if (isNaN(x)) {
    return 1;
  }
  if (x === 1 || x === 0) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
console.log(factorial(value));
