#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length === undefinied) {
  console.log('Not enough arguements');
} else {
  const arg1 = args[0];
  const arg2 = args[1];
  console.log(`${arg1} is ${arg2}`);
}
