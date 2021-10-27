"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
给一颗二叉树，返回从右边看能看到的第一个。

思路BFS，返回最后的一个即可。

beat
94 %。

测试地址：
https: // leetcode.com / problems / binary - tree - right - side - view / description /
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        if self:
            return "{} <- {} -> {}".format(repr(self.left), self.val, repr(self.right))

class Solution:
    # recursive
    def rightSideView(self, root):
        res = []
        level = 1
        self.helper(root, level, res)
        return res
    def helper(self, node, level, res):
        if not node:
            return
        if level > len(res):
            res.append(node.val)

        self.helper(node.right, level + 1, res)
        self.helper(node.left, level +1, res )
    # queue, BFS level by level
    def use_queue(self, root):
        q = collections.deque()
        res = []
        if root:
            q.append(root)

        while q:
            size, val = len(q), 0
            for _ in range(size):
                node = q.popleft()
                val = node.val # store last value in each level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(val)
        return res

#display binary tree by level
class Sol(object):
    def levelorder(self, root):
        from collections import deque
        q = deque()
        res = []
        q.append(root)
        i=0
        while q:
            temp=(i)
            i+=1
            node = q.popleft()
            res.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res