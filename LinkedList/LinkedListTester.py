from LinkedList import LinkedList

print('Running the tests... \n')

# Test add
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
assert l.to_list() == [1,2,3,4]
print('Test add ... PASSED!')

# Test add_all
l = LinkedList()
l.add_all([10,15,30,40])
assert l.to_list() == [10,15,30,40]
l.add_all([5,10])
assert l.to_list() == [10,15,30,40,5,10]
l.add_all([])
assert l.to_list() == [10,15,30,40,5,10]
print('Test add_all ... PASSED!')

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
print('Test insert ... PASSED!')

# Test insert_all
l = LinkedList()
l.add(1)
l.add(2)
l.add(3)
l.add(4)
l.insert_all(2, [10,30,50])
assert l.to_list() == [1,2,10,30,50,3,4]
print('Test insert_all ... PASSED!')

# Test contains
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
assert l.contains(5) == True
assert l.contains(11) == False
print('Test contains ... PASSED!')

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
print('Test get ... PASSED!')

# Test index_of
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
assert l.index_of(1) == 0
assert l.index_of(10) == 3
assert l.index_of(17) == -1
print('Test index_of ... PASSED!')

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
print('Test last_index_of ... PASSED!')

# Test poll
l = LinkedList()
l.add(1)
l.add(5)
l.add(10)
assert l.poll() == 1
assert l.size() == 2
assert l.poll() == 5
assert l.size() == 1
assert l.poll() == 10
assert l.size() == 0
assert l.poll() is None
assert l.size() == 0
print('Test poll ... PASSED!')

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
assert l.remove_by_index(3) == 10
assert l.size() == 5
assert l.remove_by_index(0) == 1
assert l.size() == 4
assert l.peek() == 5
assert l.remove_by_index(3)
assert l.size() == 3
print('Test remove_by_index ... PASSED!')

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
assert l.peek() == 5
assert l.remove_by_value(7) is True
assert l.size() == 4
assert l.to_list() == [5,10,5,10]
print('Test remove_by_value ... PASSED!')

# Test set
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
l.add(5)
l.add(10)
assert l.set(-1, 50) is None
assert l.set(6, 50) is None
assert l.set(3, 50) == 50
assert l.to_list() == [1,5,7,50,5,10]
assert l.set(0, 75) == 75
assert l.set(5, 100) == 100
assert l.to_list() == [75,5,7,50,5,100]
print('Test set ... PASSED!')

# Check the prinout
l = LinkedList()
l.add(1)
l.add(5)
l.add(7)
l.add(10)
l.add(5)
l.add(10)
print(l)


print('\nAll the tests passed!')
