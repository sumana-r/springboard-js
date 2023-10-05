// not async, obvs
function friendlyFn() { 
  return "hello!!! omg so nice to meet you!"
}

friendlyFn();
// "hello!!! omg so nice to meet you!"

// omg async
async function asyncFriendlyFn() {
  return "hello!!! omg so nice to meet you!"
}

asyncFriendlyFn();
// Promise {<resolved>: "hello!!! omg so nice to meet you!"}

asyncFriendlyFn().then(msg => console.log(msg));
// "hello!!! omg so nice to meet you!"

// similar behavior to async
function friendlyFnPromise() {
  return Promise.resolve("hello!!! omg so nice to meet you!")
}

friendlyFnPromise();
// Promise {<resolved>: "hello!!! omg so nice to meet you!"}

friendlyFnPromise().then(msg => console.log(msg));
// "hello!!! omg so nice to meet you!"

async function oops() {
  throw "you shouldn't have invoked me!!"
}

oops();
// Promise {<rejected>: "you shouldn't have invoked me!!"}

oops().catch(err => console.log(err));
// "you shouldn't have invoked me!!"