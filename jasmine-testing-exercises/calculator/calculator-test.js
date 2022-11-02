
it('should calculate the monthly rate correctly', function () {
  expect(calculateMonthlyPayment({amount:10000,years:2,rate:6})).toEqual('60000.00');
  expect(calculateMonthlyPayment({amount:2500,years:18,rate:32})).toEqual('20000.00');
});


it("should return a result with 2 decimal places", function() {
  expect(calculateMonthlyPayment({amount:2500,years:18,rate:32})).toEqual('20000.00');
});

/// etc
