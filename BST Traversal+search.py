class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)
    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)

def search(root, key):
    if root is None:
        return False
    if root.data == key:
        return True
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

# Create BST
root = None
for x in [50, 30, 70, 20, 40]:
    root = insert(root, x)

print("BST:")
inorder(root)

key = int(input("\nEnter value to search: "))

if search(root, key):
    print("Found")
else:
    print("Not Found")
