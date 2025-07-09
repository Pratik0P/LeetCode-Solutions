# Problem: Construct Binary Tree from Inorder and Postorder Traversal
# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(inorder, postorder):
    if not inorder or not postorder:
        return None

    root_val = postorder.pop()
    root = TreeNode(root_val)
    index = inorder.index(root_val)

    root.right = buildTree(inorder[index+1:], postorder)
    root.left = buildTree(inorder[:index], postorder)

    return root
