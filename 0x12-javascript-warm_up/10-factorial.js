#!/usr/bin/node

const args = process.argv;
const intArg = parseInt(args[2]);

/**
 * factorial - Returns the factorial of a number
 * @param {number} n - Number to calculate the factorial of
 *
 * @returns {number} - Factorial of n
 */
function factorial (n) {
  if (isNaN(n) || n === 0) {
    return 1;
  }

  return n * factorial(n - 1);
}

console.log(factorial(intArg));
