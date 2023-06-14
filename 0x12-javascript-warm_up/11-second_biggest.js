#!/usr/bin/node

const findSecondBiggest = (args) => {
  const integers = args.map(arg => parseInt(arg)).filter(num => !isNaN(num));

  if (integers.length < 2) {
    console.log('0');
    return;
  }

  const sortedIntegers = integers.sort((a, b) => b - a);
  console.log(sortedIntegers[1]);
};

const arguments = process.argv.slice(2);
findSecondBiggest(arguments);

