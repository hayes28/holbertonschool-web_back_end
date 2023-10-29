// 3. Spies - Utils

const Utils = {
  calculateNumber(type, a, b) {
    const numA = Math.round(a);
    const numB = Math.round(b);

    switch (type) {
      case 'SUM':
        return numA + numB;
      case 'SUBTRACT':
        return numA - numB;
      case 'DIVIDE':
        if (numB === 0) {
          return 'Error';
        }
        return numA / numB;
      default:
        throw new Error('Unknown operation');
    }
  }
};

module.exports = Utils;
