class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)
    
    def _insert(self, root, key):
        if key < root.val:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert(root.right, key)
    
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)