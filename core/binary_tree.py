class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    # @brief: Create a node in a tree
    # @param: start: Node with value, right and left
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    # @brief: Insert properly the node in binary tree
    # @param: start: Node with value, righ
    # @param: current_node: actual node in the binary tree
    def _insert(self, data, current_node):
        if data < current_node.value:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert(data, current_node.left)
        elif data > current_node.value:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert(data, current_node.right)
        else:
            print("El valor ya esta en el arbol")

    # @brief: Create a list of preorder traversal
    # @param: start: Node with value, right and left
    # @return: preorder list
    def preorder(self, start, traversal: list):
        "Root>left>Right"
        if start:
            traversal.append(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    # @brief: Create a list of inorder traversal
    # @param: start: Node with value, right and left
    # @return: Inorder list
    def inorder(self, start, traversal: list):
        "Left>Root>Right"
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder(start.right, traversal)
        return traversal

    # @brief: Create a list of postorder traversal
    # @param: start: Node with value, right and left
    # @return: Post Order list
    def postorder(self, start, traversal: list):
        "Left>Right>Root"
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.value)
        return traversal

    # @brief: Create a list of level order traversal
    # @param: start: Node with value, right and left
    # @return: Level order list
    def levelorder(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        traversal = []
        while len(queue) > 0:
            traversal.append(queue.peek())
            node = queue.dequeue()
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)
        return traversal

    # @brief: draw a binary tree
    # @param: start: Node with value, right and left, and level
    # @return: Drawing of binary tree
    def drawtree(self, start, level=0):
        if start is not None:
            self.drawtree(start.left, level + 1)
            print((" " * 2 * level) + "-> " + str(start.value))
            self.drawtree(start.right, level + 1)
        return ""


if __name__ == "__main__":
    pass
