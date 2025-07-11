# Problem: Invert Binary Tree
# Link: https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if not root:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
