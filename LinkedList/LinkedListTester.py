from LinkedList import LinkedList

print('Running the tests...')

# Test add
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
assert l.to_list() == [1,2,3,4]

# Test insert
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.insert(1,11)
l.insert(0,14)
l.insert(5,27)
assert l.to_list() == [14,1,11,2,3,4,27]

# Test contains
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
assert l.contains(5) == True
assert l.contains(11) == False

# Test get
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
assert l.get(-1) is None
assert l.get(4) is None
assert l.get(1) == 5
assert l.get(0) == 1
assert l.get(3) == 10

print('All the tests passed!')
