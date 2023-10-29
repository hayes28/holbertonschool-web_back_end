// Test cases chai

const expect = require('chai').expect;
const calculateNumber = require('./2-calcul_chai.js');

describe('calculateNumber', () => {
    it('should return rounded sum when type is SUM', () => {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
    });
    it('should return rounded difference when type is SUBTRACT', () => {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
    });
    it('should return rounded division when type is DIVIDE', () => {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
    });
    it('should return Error when type is DIVIDE and b is 0', () => {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
    });
});
