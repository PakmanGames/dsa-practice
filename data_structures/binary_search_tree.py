class Node:
    def __init__(self, key: int, value: int, n: int):
        self.key = key
        self.value = value
        self.left = None # Node
        self.right = None # Node
        self.n = n # Size

class SymbolTable:
    def __init__(self, root: Node):
        self.root = root # Node

    def get(self, key: int) -> int:
        return get(self.root, key)

    def min(self) -> int:
        return min(self.root)

    def max(self) -> int:
        return max(self.root)

    def put(self, key: int, value: int) -> Node:
        return put(self.root, key, value)

    def size(self):
        return size(self.root)

def get(node: Node, key: int) -> int:
    if node == None:
        return None
    if node.key < key:
        return get(node.right, key)
    elif node.key > key:
        return get(node.left, key)
    return node.value

def min(node: Node) -> int:
    if node == None:
        return None
    if node.left != None:
        return min(node.left)
    return node.value

def max(node: Node) -> int:
    if node == None:
        return None
    if node.right != None:
        return max(node.right)
    return node.value

def put(node: Node, key: int, value: int) -> Node:
    if node == None:
        return Node(key, value, 1)
    if node.key < key:
        node.right = put(node.right, key, value)
    elif node.key > key:
        node.left = put(node.left, key, value)
    else:
        node.value = value
    node.n = size(node.left) + size(node.right) + 1
    return node

def size(node: Node):
    if node == None:
        return 0
    else:
        return node.n

n = Node(8, 2, 1)
s = SymbolTable(n)
s.root = s.put(3, 2)
s.root = s.put(10, 2)
s.root = s.put(1, 4)
s.root = s.put(9, 3)
s.root = s.put(14, 5)
s.root = s.put(2, 2)

print("Min: " + str(s.min()))
print("Max: " + str(s.max()))
print("Getting a 9: " + str(s.get(9)))
print("Getting non existant: " + str(s.get(41)))
print("Getting the size: " + str(s.size()))