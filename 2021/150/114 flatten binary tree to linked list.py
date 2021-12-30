""" https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1208004/Extremely-Intuitive-O(1)-Space-solution-with-Simple-explanation-Python
"""
class Solution:
    def flatten(self, root):
        """
        1. flatten left subtree
        2. find the left subtree's tail
        3. set root's left to None, root's right to root's left, tail's right to root.right
        4. flatten the original right subtree
        :param root:
        :return:
        """
        #  escape condition
        if not root:
            return
        right = root.right
        if root.left:
            #  flatten left subtree
            self.flatten(root.left)
            #find the tail of left subtree
            tail = root.left
            while tail.right:
                tail = tail.right
            # left <- None, right <- left, tail's right <- right
            root.left, root.right, tail.right = None, root.left, right
        #flatten right subtree
        self.flatten(right)