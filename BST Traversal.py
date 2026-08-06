class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to insert a node into BST
def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root

# Inorder Traversal (Left -> Root -> Right)
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

# Preorder Traversal (Root -> Left -> Right)
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# Postorder Traversal (Left -> Right -> Root)
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

# Driver Code
root = None

n = int(input("Enter number of nodes: "))

print("Enter node values:")
for i in range(n):
    value = int(input())
    root = insert(root, value)

print("\nInorder Traversal:")
inorder(root)

print("\nPreorder Traversal:")
preorder(root)

print("\nPostorder Traversal:")
postorder(root)
