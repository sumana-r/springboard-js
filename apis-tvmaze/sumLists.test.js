const LinkedList = require("./sumLists");

describe("#sumLists", function () {
  test("it works on even sized lists", function () {
    const listOne = new LinkedList();
    const listTwo = new LinkedList();

    listOne.push(5);
    listOne.push(6);
    listOne.push(3);

    listTwo.push(8);
    listTwo.push(4);
    listTwo.push(2);

    const result = LinkedList.sumLists(listOne, listTwo);
    const expected = new LinkedList();
    expected.push(3);
    expected.push(1);
    expected.push(6);
    expect(result).toEqual(expected);
  });

  test("it works on uneven sized lists", function () {
    const listThree = new LinkedList();
    const listFour = new LinkedList();

    listThree.push(7);
    listThree.push(5);
    listThree.push(9);
    listThree.push(4);
    listThree.push(6);

    listFour.push(8);
    listFour.push(4);

    const result = LinkedList.sumLists(listThree, listFour);
    const expected = new LinkedList();
    expected.push(5);
    expected.push(0);
    expected.push(0);
    expected.push(5);
    expected.push(6);
    expect(result).toEqual(expected);
  });

  test("it carrys over an extra one", function () {
    const listThree = new LinkedList();
    const listFour = new LinkedList();

    listThree.push(9);
    listThree.push(9);
    listThree.push(9);

    listFour.push(1);

    const expected = new LinkedList();
    expected.push(0);
    expected.push(0);
    expected.push(0);
    expected.push(1);

    const result = LinkedList.sumLists(listThree, listFour);
    expect(result).toEqual(expected);
  });

  test("it passes the sample case", function () {
    const l1 = new LinkedList();
    const l2 = new LinkedList();

    l1.push(4);
    l1.push(6);
    l1.push(3);

    l2.push(7);
    l2.push(2);
    l2.push(1);

    const expected = new LinkedList();
    expected.push(1);
    expected.push(9);
    expected.push(4);

    const result = LinkedList.sumLists(l1, l2);
    expect(result).toEqual(expected);
  });
});
