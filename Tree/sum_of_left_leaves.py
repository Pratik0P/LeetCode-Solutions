# Problem: Sum of Left Leaves
# Link: https://leetcode.com/problems/sum-of-left-leaves/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root):
    if not root:
        return 0

    total = 0
    if root.left and not root.left.left and not root.left.right:
        total += root.left.val

    return total + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
