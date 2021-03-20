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

print('All the tests passed!')
