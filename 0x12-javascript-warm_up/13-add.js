#!/usr/bin/node

const args = process.argv;
const num1 = parseInt(args[2]);
const num2 = parseInt(args[3]);

/**
 * add - returns the sum of two numbers
 * @param {number} a - first number
 * @param {number} b - second number
 * @returns {number} - sum of a and b
 */
function add(a, b) {
    return a + b;
}

exports.add = add;
