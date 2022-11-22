const { Tree, Node } = require("./countValidWords");

describe("#countValidWords", function () {
  let tree;
  let node1;
  let node2;
  let node3;
  let node4;
  let node5;
  let node6;
  it("counts stops early", function () {
    node6 = new Node("excellent");
    node5 = new Node("done");
    node4 = new Node("nice", node5, node6);
    node3 = new Node("yes", node4);
    node2 = new Node("awesome", node3);
    node1 = new Node("STOP", null, node2);
    tree = new Tree(node1);
    expect(tree.countValidWords()).toEqual(0);
  });
  it("counts valid words early", function () {
    node6 = new Node("excellent");
    node5 = new Node("done");
    node4 = new Node("STOP", node5, node6);
    node3 = new Node("yes", node4);
    node2 = new Node("awesome", node3);
    node1 = new Node("awesome", null, node2);
    tree = new Tree(node1);
    expect(tree.countValidWords()).toEqual(3);
  });
});
