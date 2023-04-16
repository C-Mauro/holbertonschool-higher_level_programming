#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (x) {
  for (let i = 0; i < x; i++) { console.log('C is Fun'); }
} else {
  console.log('Missing number of occurrences');
}
