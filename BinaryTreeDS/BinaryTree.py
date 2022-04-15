from BinaryTreeDS.BinaryTreeNode import BinaryTreeNode

class BinaryTree:
    def __init__(self):
        self.root = None
        self.num_nodes = 0

    def add(self, value):
        self.__add_helper__(self.root, value)

    def __add_helper__(self, node, value):
        if not node:
            self.root = BinaryTreeNode(value)
            return

        q = [node]

        # Level order traversal until finding empty spot
        while len(q):
            temp = q[0]
            q.pop(0)

            # If left is empty add node here, otherwise add to queue
            if not temp.left:
                temp.left = BinaryTreeNode(value)
                break
            q.append(temp.left)

            # If right is empty add node here, otherwise add to queue
            if not temp.right:
                temp.right = BinaryTreeNode(value)
                break
            q.append(temp.right)

        self.num_nodes += 1

    def remove(self, value):
        if not self.contains(value):
            return None





    def contains(self, value):
        if not self.root:
            return False

        q = [self.root]

        # Level order traversal until finding empty spot
        while len(q):
            temp = q[0]
            q.pop(0)

            # Check for match
            if temp.val == value:
                return True

            # Check if left exists
            if temp.left:
                q.append(temp.left)

            # Check if right exists
            if temp.right:
                q.append(temp.right)

        return False

    def get_root(self):
        return self.root

    def depth(self):
        if self.root is None:
            return 0

        return self.__depth_helper(self.root) - 1

    def __depth_helper(self, node):
        if not node:
            return 0

        return 1 + max(self.__depth_helper(node.left), self.__depth_helper(node.right))

    def size(self):
        return self.num_nodes

    def pre_order(self):
        values = []
        self.__pre_order_helper__(self.root, values)
        return values

    def __pre_order_helper__(self, node, values):
        if not node:
            return

        values.append(node.val)
        self.__pre_order_helper__(node.left, values)
        self.__pre_order_helper__(node.right, values)

    def post_order(self):
        values = []
        self.__post_order_helper__(self.root, values)
        return values

    def __post_order_helper__(self, node, values):
        if not node:
            return

        self.__post_order_helper__(node.left, values)
        self.__post_order_helper__(node.right, values)
        values.append(node.val)

    def in_order(self):
        values = []
        self.__in_order_helper__(self.root, values)
        return values

    def __in_order_helper__(self, node, values):
        if not node:
            return

        self.__in_order_helper__(node.left, values)
        values.append(node.val)
        self.__in_order_helper__(node.right, values)

    def __str__(self):
        retStr = ''

        # Base case
        if self.root is None:
            return
        # Create an empty queue for level order traversal
        q = []

        # Enqueue root and initialize height
        q.append(self.root)

        while q:

            # nodeCount (queue size) indicates number
            # of nodes at current lelvel.
            count = len(q)

            # Dequeue all nodes of current level and
            # Enqueue all nodes of next level
            while count > 0:
                temp = q.pop(0)
                retStr += str(temp.val) + ' '
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)

                count -= 1

            retStr += '\n'
        return retStr