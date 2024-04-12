#!/usr/bin/node

const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

/**
 * add - returns the sum of two numbers
 * @param {number} a
 * @param {number} b
 * @returns {number} - sum of a and b
 */
function add (a, b) {
  return a + b;
}

if (isNaN(num1) || isNaN(num2)) {
  console.log('NaN');
} else {
  console.log(add(num1, num2));
}
