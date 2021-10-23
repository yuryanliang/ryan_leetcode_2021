"""
Given a binary tree, return the preorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,2,3]
Follow up: Recursive solution is trivial, could you do it iteratively?
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if not root:
            return
        res.append(root.val)
        self.helper(root.left, res)
        self.helper(root.right, res)

    # stack
    def preorder_1(self,root):
        res=[]
        node = root
        stack = [root]
        while stack:
            if node:
                stack.append(node)
                res.append(node.val)
                node = node.left
            else:
                temp = stack.pop()
                node = temp.right
        return res
