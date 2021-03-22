from ListNode import ListNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elems = 0

    def add(self, value):
        newNode = ListNode(value)
        if self.num_elems == 0:
            self.head = newNode
            self.tail = newNode
        elif self.num_elems == 1:
            self.head.next = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

        self.num_elems += 1

    def insert(self, index, value):
        if index >= self.num_elems or index < 0:
            return

        newNode = ListNode(value)

        if index == 0:
            self.add_first(value)
            return

        if index == self.num_elems - 1:
            self.add(value)
            return

        curr = self.head
        for i in range(index - 1):
            curr = curr.next

        newNode.next = curr.next
        curr.next = newNode

        self.num_elems += 1

    def add_all(self, values):
        raise NotImplementedError('Need to implement')

    def insert_all(self, index, value):
        raise NotImplementedError('Need to implement')

    def add_first(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode
        self.num_elems += 1

    def add_last(self, value):
        self.add(value)

    def clear(self):
        self.head = None
        self.tail = None
        self.num_elems = 0

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
        if index < 0 or index >= self.num_elems:
            return None
        curr = self.head
        for i in range(index):
            curr = curr.next
        return curr.val

    def get_first(self):
        return self.head

    def get_last(self):
        return self.tail

    def index_of(self, value):
        index = 0
        curr = self.head
        while curr != None:
            if curr.val == value:
                return index
            index += 1
            curr = curr.next
        return -1

    def last_index_of(self, value):
        index = 0
        matching = -1
        curr = self.head
        while curr is not None:
            if curr.val == value:
                matching = index
            index += 1
            curr = curr.next
        return matching

    def peek(self):
        return self.head

    def poll(self):
        if self.head == None:
            return None

        ret = self.head
        if self.head.next == None:
            self.head = None
            self.num_elems = 0
        else:
            self.head = self.head.next
            self.num_elems -= 1

        return ret

    def remove_head(self):
        self.poll()

    def remove_by_index(self, index):
        if index < 0 or index >= self.num_elems:
            return None

        if index == 0:
            return self.poll()

        curr = self.head
        for i in range(1,index):
            curr = curr.next

        ret = curr.next
        curr.next = curr.next.next
        if index == self.num_elems -1:
            self.tail = curr
        self.num_elems -= 1

        return ret


    def remove_by_value(self, value):
        if self.num_elems == 0:
            return False

        if self.head.val == value:
            self.poll()
            return True

        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.val == value:
                prev.next = curr.next
                self.num_elems -= 1
                return True
            prev = curr
            curr = curr.next

        return False


    def set(self, index, value):
        raise NotImplementedError('Need to implement')

    def size(self):
        return self.num_elems

    def to_list(self):
        as_list = []
        curr = self.head
        while curr != None:
            as_list.append(curr.val)
            curr = curr.next
        return as_list

    def __str__(self):
        raise NotImplementedError('Need to implement')