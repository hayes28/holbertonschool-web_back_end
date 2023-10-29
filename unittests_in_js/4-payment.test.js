// Test cases for payment - STUBS
const expect = require('chai').expect;
const sinon = require('sinon');
const sendPaymentRequestToApi = require('./3-payment');
const Utils = require('./utils');

describe('sendPaymentRequestToApi', () => {
    it('should return 200 if the payment is successful', () => {
        // Stub Utils.calculateNumber to always return 10
        const stub = sinon.stub(Utils, 'calculateNumber').returns(10);

        // Spy on console.log to check if it logs the correct message
        const logSpy = sinon.spy(console, 'log');

        sendPaymentRequestToApi(100, 20);
        // Check if stub was called correctly
        expect(stub.calledOnceWithExactly('SUM', 100, 20)).to.be.true;

        // Check if console.log was called with the correct message
        expect(logSpy.calledOnceWithExactly('The total is: 10')).to.be.true;
        stub.restore();
        logSpy.restore();
    });
});
