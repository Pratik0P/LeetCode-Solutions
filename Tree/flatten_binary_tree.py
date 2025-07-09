# Problem: Flatten Binary Tree to Linked List
# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root):
    if not root:
        return

    flatten(root.left)
    flatten(root.right)

    temp_right = root.right
    root.right = root.left
    root.left = None

    current = root
    while current.right:
        current = current.right
    current.right = temp_right
