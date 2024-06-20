#!/usr/bin/node

if (isNaN(Math.floor(Number(process.argv[2])))) {
  console.log('Not a number');
} else {
  console.log(`My number: ${process.argv[2]}`);
}
