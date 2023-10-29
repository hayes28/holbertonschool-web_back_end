// Test caes for the api.js file
const request = require('request');
const { expect } = require('chai');

describe('Index page', function () {
    it('should return correct status code', function (done) {
        request('http://localhost:7865', function (error, response, body) {
            expect(response.statusCode).to.equal(200);
            done();
        });
    });

    it('should return correct result', function (done) {
        request('http://localhost:7865', function (error, response, body) {
            expect(body).to.equal('Welcome to the payment system');
            done();
        });
    });

    it('should return 404 when :id is NOT a number', function (done) {
        request('http://localhost:7865/cart/hello', function (error, response, body) {
            expect(response.statusCode).to.equal(404);
            done();
        });
    });
});
