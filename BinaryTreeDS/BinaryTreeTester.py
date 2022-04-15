from BinaryTreeDS.BinaryTree import BinaryTree

print('Running the tests... \n')

# Test add
tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
assert [4, 2, 5, 1, 3] == tree.in_order()
print('Test add ... PASSED!')

# Test contains
tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
assert tree.contains(1) is True
assert tree.contains(2) is True
assert tree.contains(5) is True
assert tree.contains(7) is False
print('Test contains ... PASSED!')

# Test depth
tree = BinaryTree()
assert tree.depth() == 0
tree.add(1)
assert tree.depth() == 0
tree.add(2)
tree.add(3)
assert tree.depth() == 1
tree.add(4)
tree.add(5)
assert tree.depth() == 2
print('Test depth ... PASSED!')

# Test different order traversals
tree = BinaryTree()
tree.add(1)
tree.add(2)
tree.add(3)
tree.add(4)
tree.add(5)
assert [4, 2, 5, 1, 3] == tree.in_order()
assert [1, 2, 4, 5, 3] == tree.pre_order()
assert [4, 5, 2, 3, 1] == tree.post_order()
print('Test traversals passed ... PASSED!')
