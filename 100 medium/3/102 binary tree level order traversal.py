""" https://leetcode.com/problems/binary-tree-level-order-traversal/
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""

"""
用deque 结构

先把root 压入，
while q 的循环
popleft， 放入res/， 压入left， 压入right
"""
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        if self:
            return "{} <- {} -> {}".format(repr(self.left), self.val, repr(self.right))

class Solution:
    def levelOrder(self, root):
        from collections import deque  #  deque.pop, deque.popleft, deque.append
        q = deque()
        q.append(root)

        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return res

class Sol:
    def levelOrder(self, root):
        from collections import deque
        q = deque()
        q.append((root, 0))

        res = []
        res_set = set()

        while q:
            node, level = q.popleft()
            if node:
                if level not in res_set:
                    res_set.add(level)
                    res.append([])
                res[level].append(node.val)
                q.append((node.left, level + 1))
                q.append((node.right, level + 1))

        return res

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    result = Solution().levelOrder(root)
    print (result)