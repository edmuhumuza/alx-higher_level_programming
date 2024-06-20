#!/usr/bin/node
const y = 0;
if (process.argv.length <= 2) {
  console.log(y);
} else if (process.argv.length === 3) {
  console.log(y);
} else {
  const array = [];
  for (let x = 2; x < process.argv.length; x++) {
    if (Number(process.argv[x])) {
      array.push(Number(process.argv[x]));
    }
  }
  const newArray = array.sort((a, b) => a - b);
  console.log(newArray[newArray.length - 2]);
}
