#!/usr/bin/node
const square = Math.floor(Number(process.argv[2]));

if (isNaN(square)) {
  console.log('Missing size');
} else if (square < 0) {
  // No operation
} else {
  for (let y = 0; y < square; y++) {
    for (let z = 0; z < square; z++) {
      process.stdout.write('X');
    }
    console.log();
  }
}
