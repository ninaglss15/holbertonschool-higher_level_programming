#!/usr/bin/node
const args = process.argv.slice(2).map(n => parseInt(n));

if (args.length < 2) {
  console.log(0);
} else {
  let max = Math.max(...args);
  let filtered = args.filter(n => n !== max);
  let secondMax = filtered.length > 0 ? Math.max(...filtered) : 0;
  console.log(secondMax);
}
