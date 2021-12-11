""" https://leetcode.com/problems/recover-binary-search-tree/
You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.



Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1


https://leetcode.com/problems/recover-binary-search-tree/discuss/187407/Python-short-and-slick-solution-(108ms-beats-100)-both-stack-and-Morris-versions
Explanation
I don't have any new ideas; just a cool way to implement an old idea.

Use whatever inorder traversal you like (recursion/stack = O(log n) extra space, Morris = O(1) extra space). As most people have figured out pretty easily, the idea is to remember the last value you saw and compare it with the current value. If lastValue > currentValue, then we know that something is "wrong", but it's not immediately clear which values have to be swapped.

There are 2 cases: The values that need to be swapped are either adjacent or not adjacent. If they're adjacent, then there will be one "drop"; if they're not adjacent, then there will be two "drops".

adjacent: ... _ < _ < A > B < _ < _ ...
                      ^^^^^
                      drop #1

not adjacent: ... _ < _ < A > X < _ < Y > B < _ < _ ... (X may be the same as Y, but it's irrelevant)
                          ^^^^^       ^^^^^
                          drop #1     drop #2
In both cases, we want to swap A and B. So the idea is to keep a drops array and append a tuple of (lastNode, currentNode) whenever we come across lastValue > currentValue. At the end of the traversal, the drops array must have either 1 or 2 tuples (otherwise, there would be more than 2 nodes that need to be swapped).

Here's the clear but not-so-clean way to swap them:

if len(drops) == 1: # drops == [(A, B)]
    drops[0][0].val, drops[0][1].val = drops[0][1].val, drops[0][0].val
else: # drops == [(A, X), (Y, B)]
    drops[0][0].val, drops[1][1].val = drops[1][1].val, drops[0][0].val
"""
class Solution:
    def recoverTree(self, root):
        cur = root
        prev = TreeNode(float('-inf'))
        stack = []
        drops = []
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            node= stack.pop()
            if node.val < prev.val:
                drops.append((prev, cur))
            prev, cur = node, node.right
        if len(drops) == 1: # drops == [(A, B)]
            drops[0][0].val, drops[0][1].val = drops[0][1].val, drops[0][0].val
        else: # drops == [(A, X), (Y, B)]
            drops[0][0].val, drops[1][1].val = drops[1][1].val, drops[0][0].val