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

# Test index_of
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
assert l.index_of(1) == 0
assert l.index_of(10) == 3
assert l.index_of(17) == -1

# Test last_index_of
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
l.add(5)
l.add(10)
assert l.last_index_of(1) == 0
assert l.last_index_of(10) == 5
assert l.last_index_of(7) == 2
assert l.last_index_of(35) == -1

# Test poll
l = LinkedList()
l.add(1)
l.add(5)
l.add(10)
assert l.poll().val == 1
assert l.size() == 2
assert l.poll().val == 5
assert l.size() == 1
assert l.poll().val == 10
assert l.size() == 0
assert l.poll() is None
assert l.size() == 0

# Test remove_by_index
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
l.add(5)
l.add(10)
assert l.remove_by_index(-1) is None
assert l.remove_by_index(6) is None
assert l.remove_by_index(3).val == 10
assert l.size() == 5
assert l.remove_by_index(0).val == 1
assert l.size() == 4
assert l.peek().val == 5
assert l.remove_by_index(3)
assert l.size() == 3


# Test remove_by_value
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
l.add(5)
l.add(10)
assert l.remove_by_value(11) is False
assert l.remove_by_value(1) is True
assert l.size() == 5
assert l.peek().val == 5
assert l.remove_by_value(7) is True
assert l.size() == 4
assert l.to_list() == [5,10,5,10]

print('All the tests passed!')
