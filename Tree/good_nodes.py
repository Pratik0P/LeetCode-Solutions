# Problem: Count Good Nodes in Binary Tree
# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        res = 1 if node.val >= max_val else 0
        max_val = max(max_val, node.val)
        res += dfs(node.left, max_val)
        res += dfs(node.right, max_val)
        return res

    return dfs(root, root.val)
