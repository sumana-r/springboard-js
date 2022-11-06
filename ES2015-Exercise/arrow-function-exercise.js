// ES5 Callback

/*function double(arr) {
    return arr.map(function(val) {
      return val * 2;
    });*/


  //// ES2015 Arrow Functions Shorthand

  function double(arr){
    return arr.map((val)=> val *2 )
  }
    // function with parentheses
   const double1 = (arr) => arr.map((val)=> val *2 )

    // function without parentheses
   const double2 = arr => arr.map((val)=> val *2 )
  
//Refactor the following function to use arrow functions:

/*function squareAndFindEvens(numbers){
    var squares = numbers.map(function(num){
      return num ** 2;
    });
    var evens = squares.filter(function(square){
      return square % 2 === 0;
    });
    return evens;
  }*/

  function squareAndFindEvens(numbers){
    var squares = numbers.map(num => num ** 2);
      
    var evens = squares.filter(square => (square % 2 === 0)) 
     
     return evens;
  }
  // function without parentheses
  const squareAndFindEvens1 = numbers => numbers.map(num => num ** 2).filter(square => square % 2 === 0);