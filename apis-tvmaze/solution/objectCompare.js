function sameArrays(arr1, arr2) {
  // return true if every value is the same in the other at the specified index
  if (arr1.length !== arr2.length) return false;
  // make sure that every value in the array is the same as the other at the same index
  return arr1.every((val, idx) => {

    // nested arrays? recurse!
    if (Array.isArray(val)) {
      return sameArrays(val, arr2[idx]);
    }
    // arrays with objects in them, call our sameObjects fn!
    if (val instanceof Object && arr2[idx] instanceof Object) {
      return sameObjects(val, arr2[idx])
    }
    return val === arr2[idx];
  });
}

function sameObjects(obj1, obj2) {
  // if the size of the keys is different, return false
  if (Object.keys(obj1).length !== Object.keys(obj2).length){
    return false
  }
  // loop through each key and make sure it exists
  for (let key in obj1) {
    if (obj2[key] === undefined) {
      return false;
    }
    // are we comparing two arrays? use our helper again!
    else if (Array.isArray(obj1[key]) && Array.isArray(obj2[key])) {
      // if they are both arrays let's see if the values are different
      if (sameArrays(obj1[key], obj2[key]) === false) {
        // if so, return false
        return false;
      }
    }
    // are we comparing two objects? recurse!
    else if (obj1[key] instanceof Object && obj2[key] instanceof Object){
      return sameObjects(obj1[key], obj2[key])
    }
    // finally, let's make sure the values are the same
    else if (obj1[key] !== obj2[key]) {
      return false;
    }
  }
  return true
}

function objectCompare(obj1, obj2) {
  // both arrays? use our helper function!
  if (Array.isArray(obj1) && Array.isArray(obj2)) {
    return sameArrays(obj1, obj2);
  }
  return sameObjects(obj1,obj2)
}

module.exports = objectCompare