from ListNode import ListNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        newNode = ListNode(value)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        elif self.size == 1:
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.size += 1

    def insert(self, index, value):
        if index >= self.size or index < 0:
            return

        newNode = ListNode(value)

        if index == 0:
            self.add_first(value)
            return

        if index == self.size - 1:
            self.add(value)
            return

        curr = self.head
        for i in range(index - 1):
            curr = curr.next

        newNode.next = curr.next
        curr.next = newNode

        self.size += 1

    def add_all(self, values):
        raise NotImplementedError('Need to implement')

    def insert_all(self, index, value):
        raise NotImplementedError('Need to implement')

    def add_first(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def add_last(self, value):
        self.add(value)

    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

    def contains(self, value):
        curr = self.head
        while curr is not None:
            if curr.val == value:
                return True
            curr = curr.next
        return False

    def element(self):
        return self.head

    def get(self, index):
        raise NotImplementedError('Need to implement')

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def index_of(self, value):
        raise NotImplementedError('Need to implement')

    def last_index_of(self, value):
        raise NotImplementedError('Need to implement')

    def peek(self):
        raise NotImplementedError('Need to implement')

    def poll(self):
        raise NotImplementedError('Need to implement')

    def remove_head(self):
        raise NotImplementedError('Need to implement')

    def remove_by_index(self, index):
        raise NotImplementedError('Need to implement')

    def remove_by_value(self, value):
        raise NotImplementedError('Need to implement')

    def set(self, index, value):
        raise NotImplementedError('Need to implement')

    def size(self):
        return self.size

    def to_list(self):
        as_list = []
        curr = self.head
        while curr != None:
            as_list.append(curr.val)
            curr = curr.next
        return as_list

    def __str__(self):
        raise NotImplementedError('Need to implement')