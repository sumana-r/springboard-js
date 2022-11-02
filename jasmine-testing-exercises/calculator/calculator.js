window.addEventListener('DOMContentLoaded', function() {
  const form = document.getElementById("calc-form");
  if (form) {
    setupIntialValues();
    form.addEventListener("submit", function(e) {
      e.preventDefault();
      update();
    });
  }
  
});

function getCurrentUIValues() {
  return {
    amount: +(document.getElementById("loan-amount").value),
    years: +(document.getElementById("loan-years").value),
    rate: +(document.getElementById("loan-rate").value),
  }
}





// Get the inputs from the DOM.
// Put some default values in the inputs
// Call a function to calculate the current monthly payment
function setupIntialValues() {
  document.getElementById("loan-amount").value = 10000;
  document.getElementById("loan-years").value = 2;
  document.getElementById("loan-rate").value = 6;
  update();
}

// Get the current values from the UI
// Update the monthly payment
function update() {
  const loanValues = getCurrentUIValues();
  let monthlyPayment = calculateMonthlyPayment(loanValues);
  updateMonthly(monthlyPayment);
  
}
// Given an object of values (a value has amount, years and rate ),
// calculate the monthly payment.  The output should be a string
// that always has 2 decimal places.
function calculateMonthlyPayment(values) {
  console.log(values);
  const instRate = values.rate % 12;
  const paymentNo = values.years * 12;
  const monthPay = ((values.amount * instRate) / (1-((1+instRate)**-paymentNo))).toFixed(2);
  return monthPay + '';
}

// Given a string representing the monthly payment value,
// update the UI to show the value.
function updateMonthly(monthly) {
  const getpayment = document.getElementById("monthly-payment");
  getpayment.innerHTML = "";

  getpayment.append(monthly);
}
