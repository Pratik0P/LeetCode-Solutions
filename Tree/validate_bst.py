# Problem: Validate Binary Search Tree
# Link: https://leetcode.com/problems/validate-binary-search-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    def helper(node, low=float('-inf'), high=float('inf')):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (helper(node.left, low, node.val) and
                helper(node.right, node.val, high))
    return helper(root)
