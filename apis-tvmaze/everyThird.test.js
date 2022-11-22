const everyThird = require("./everyThird");

describe("#everyThird", function () {
  it("returns a new list of every third", function () {
    expect(everyThird([1, 2, 3, 4, 5, 6, 7, 8, 9])).toEqual([3, 6, 9]);
    expect(everyThird([1, 2, 3, 4, 5, 6, 7])).toEqual([3, 6]);
    expect(everyThird([1, 2, 3, 4])).toEqual([3]);
    expect(everyThird([1, 2])).toEqual([]);
    expect(everyThird([])).toEqual([]);
  });
});
