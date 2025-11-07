#!/usr/bin/node
function add (a, b) {
  return a + b;
}
const argv = process.argv;
const a = parseInt(argv[2]);
const b = parseInt(argv[3]);
if (isNaN(a) || isNaN(b)) {
  console.log('NaN');
} else {
  console.log(add(a, b));
}