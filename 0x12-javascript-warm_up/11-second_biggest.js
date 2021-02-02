#!/usr/bin/node
let args = process.argv.slice(1);
const len = args.length;
if (len < 3) {
  console.log('0');
} else {
  args = args.sort(function (a, b) { return a - b; });
  console.log(args[len - 2]);
}
