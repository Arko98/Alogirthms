class Node:
  def __init__(self, value):
    self.val = value
    self.left = None
    self.right = None

def preorder(root):
  if root:
    print(root.val,end = ' ')
    preorder(root.left)
    preorder(root.right)
   
# Tree Definition
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Driver Code
print("Preorder Traversal of Tree:")
preorder(root)
