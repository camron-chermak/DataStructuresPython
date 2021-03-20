from LinkedList import LinkedList

print('Running the tests...')

# Test add
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
assert l.to_list() == [1,2,3,4]

print('All the tests passed!')
