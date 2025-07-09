# Problem: Binary Tree Maximum Path Sum
# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum
        if not node:
            return 0
        left = max(dfs(node.left), 0)
        right = max(dfs(node.right), 0)
        max_sum = max(max_sum, left + right + node.val)
        return max(left, right) + node.val

    dfs(root)
    return max_sum
