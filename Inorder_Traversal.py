class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def inorder(root):
  if root:
    inorder(root.left)
    print(root.val, end = ' ')
    inorder(root.right)
 
# Tree Definition
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Driver Code
print("Inorder Traversal of Tree:")
inorder(root)
