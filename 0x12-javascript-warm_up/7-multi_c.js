#!/usr/bin/node
if (process.argv[2] > 0) {
  for (let x = 0; x < process.argv[2]; x++) {
    console.log('C is fun');
  }
} else if (process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else if (process.argv[2] < 0) {
  // No operation
}
