#!/usr/bin/node

const argsCount = process.argv[2];

if (argsCount === undefined) {
  console.log('No argument');
} else {
  console.log(argsCount);
}