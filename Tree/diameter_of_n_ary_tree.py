# Problem: Diameter of N-Ary Tree
# Link: https://leetcode.com/problems/n-ary-tree-diameter/

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []

def diameter(root):
    result = 0

    def dfs(node):
        nonlocal result
        if not node:
            return 0

        top_two = [0, 0]
        for child in node.children:
            depth = dfs(child)
            if depth > top_two[0]:
                top_two[1] = top_two[0]
                top_two[0] = depth
            elif depth > top_two[1]:
                top_two[1] = depth

        result = max(result, top_two[0] + top_two[1])
        return top_two[0] + 1

    dfs(root)
    return result
