const arrayContains = require("./arrayContains");

describe("#arrayContains", function () {
  it("compares nested objects etc", function () {
    let nums = [1, 2, 3, 7, 9];
    expect(arrayContains(nums, 7)).toBe(true);

    nums = [1, 2, 3, 9];
    expect(arrayContains(nums, 7)).toBe(false);

    nums = [1, [1, [1, 7], 1]];
    expect(arrayContains(nums, 7)).toBe(true);

    nums = [1, [1, 2, [1, 2]]];
    expect(arrayContains(nums, 7)).toBe(false);
  });
});
