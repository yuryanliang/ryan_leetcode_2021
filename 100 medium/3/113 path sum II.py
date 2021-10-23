""" https://leetcode.com/problems/path-sum-ii/
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

"""
DFS， 
init res, path, cur_sum
传入node target

如果到达底层， 看meet target 不
call left
call right

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# DFS
class Solution:
    def pathSum(self, root, target):
        res = []
        path = []
        self.dfs(root, target, path, res)
        return res
    def dfs(self, root, target, path, res):
        if root:
            if not root.left and not root.right and target ==root.val:
                path.append(root.val)
                res.append(path)
            self.dfs(root.left, target - root.val, path + [root.val], res)
            self.dfs(root.right, target -root.val, path + [root.val], res)

# DFS + stack:
    def pathSum2(self, root, target):
        res = []
        stack = [(root, [root.val])]
        while stack:
            curr, path = stack.pop()
            if not curr.left and not curr.right and sum(path) == target:
                res.append(path)
            if curr.right:
                stack.append((curr.right, path+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, path+[curr.left.val]))
        return res


if __name__ == "__main__":
    root = TreeNode(5)

    print (Solution().pathSum(root, 5))