# Problem: Path Sum
# Link: https://leetcode.com/problems/path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False
    if not root.left and not root.right:
        return targetSum == root.val
    return (hasPathSum(root.left, targetSum - root.val) or
            hasPathSum(root.right, targetSum - root.val))
