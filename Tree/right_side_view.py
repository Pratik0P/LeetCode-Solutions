# Problem: Binary Tree Right Side View
# Link: https://leetcode.com/problems/binary-tree-right-side-view/

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    if not root:
        return []

    queue = deque([root])
    res = []

    while queue:
        level_length = len(queue)
        for i in range(level_length):
            node = queue.popleft()
            if i == level_length - 1:
                res.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return res
