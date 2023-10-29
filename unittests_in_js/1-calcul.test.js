// Test cases

const assert = require('assert');
const calculateNumber = require('./1-calcul.js');

describe('calculateNumber', () => {
  it('should return rounded sum when type is SUM', () => {
    assert.strictEqual(calculateNumber('SUM', 1.4, 4.5), 6);
  });
  it('should return rounded difference when type is SUBTRACT', () => {
    assert.strictEqual(calculateNumber('SUBTRACT', 5.8, 2.4), 4);
  });
  it('should return rounded division when type is DIVIDE', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 9.2, 2.8), 3);
  });
  it('should return Error when type is DIVIDE and b is 0', () => {
    assert.strictEqual(calculateNumber('DIVIDE', 9.2, 0), 'Error');
  });
});
