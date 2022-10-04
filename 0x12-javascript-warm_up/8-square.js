#!/usr/bin/node

const y = process.argv[2];
if (isNaN(y)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < y; i++) {
    console.log('X'.repeat(y));
  }
}
