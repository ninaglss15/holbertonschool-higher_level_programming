#!/usr/bin/node
const argv = process.argv;
if (argv.length <= 3) {
  console.log(0);
} else {
  const nums = [];
  for (let i = 2; i < argv.length; i++) {
    nums.push(parseInt(argv[i]));
  }
  nums.sort((a, b) => b - a);
  console.log(nums[1]);
}