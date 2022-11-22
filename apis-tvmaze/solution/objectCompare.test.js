const objectCompare = require("./objectCompare");

describe("#objectCompare", function () {
  beforeAll(function () {
    JSON.stringify = new Error("Do not use JSON.stringify");
  });

  it("compares nested objects etc", function () {
    var obj1 = { 1: [1, 2, 3, [4, { a: [1] }]] };
    var obj2 = { 1: [1, 2, 3, [4, { a: [1] }]] };
    expect(objectCompare(obj1, obj2)).toEqual(true);

    var obj1 = { 1: [1, 3, 2, [4, { a: [1] }]] };
    var obj2 = { 1: [1, 2, 3, [4, { a: [1] }]] };
    expect(objectCompare(obj1, obj2)).toEqual(false);

    var obj1 = { 1: [1, 2, 3, [4, { a: [1, 2] }]] };
    var obj2 = { 1: [1, 2, 3, [4, { a: [1] }]] };
    expect(objectCompare(obj1, obj2)).toEqual(false);

    var obj1 = { 1: [{ 1: 1 }, 2, 3, [4, { a: [1, 2] }]] };
    var obj2 = { 1: [1, 2, 3, [4, { a: [1] }]] };
    expect(objectCompare(obj1, obj2)).toEqual(false);

    var obj1 = [{ a: 1 }, 2, 3, [{ a: 1 }]];
    var obj2 = [{ a: 1 }, 2, 3, [{ a: 1 }]];
    expect(objectCompare(obj1, obj2)).toEqual(true);

    var obj1 = [{ a: 1 }, 2, 3, [{ a: 1 }]];
    var obj2 = [{ a: 1 }, 2, 3, [{ a: 1, b: 2 }]];
    expect(objectCompare(obj1, obj2)).toEqual(false);

    var obj1 = [
      { a: 1, b: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }], g: [2, 3, [{ a: 1 }]] },
    ];
    var obj2 = [
      {
        a: 1,
        b: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }],
        g: [2, 3, [{ a: 1 }]],
      },
    ];
    expect(objectCompare(obj1, obj2)).toEqual(true);

    var obj1 = [
      { a: 1, b: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }], g: [2, 3, [{ a: 1 }]] },
    ];
    var obj2 = [
      {
        a: 1,
        b: [{ c: 2, g: [3, 4, { d: 6, f: 7 }, 1] }],
        g: [2, 3, [{ a: 1 }]],
      },
    ];
    expect(objectCompare(obj1, obj2)).toEqual(false);

    var obj1 = [
      {
        a: 1,
        b: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }],
        g: [2, 3, [{ a: 1 }]],
      },
    ];
    var obj2 = [
      {
        a: 1,
        b: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }],
        g: [2, 3, [{ a: 1, b: 2 }]],
      },
    ];
    expect(objectCompare(obj1, obj2)).toEqual(false);

    var obj1 = {
      a: 1,
      b: { 1: 1, 2: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }] },
      g: [2, 3, [{ a: 1 }]],
      h: 1,
    };
    var obj2 = {
      a: 1,
      b: { 1: 1, 2: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }] },
      g: [2, 3, [{ a: 1 }]],
      h: 1,
    };
    expect(objectCompare(obj1, obj2)).toEqual(true);

    var obj1 = {
      a: 1,
      b: { 1: 1, 2: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }] },
      g: [2, 3, [{ a: 1 }]],
      h: 1,
    };
    var obj2 = {
      a: 1,
      b: { 1: 1, 2: [{ c: 2, g: [3, 4, { d: 6, f: 7 }] }] },
      g: [2, 3, [{ a: 1 }]],
      h: 1,
      i: 2,
    };
    expect(objectCompare(obj1, obj2)).toEqual(false);
  });
});
