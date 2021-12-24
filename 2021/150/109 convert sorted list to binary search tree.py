"""https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.



Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []


Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-105 <= Node.val <= 105
"""
class Solution:
    def sortedListToBST(self, head):
        def convertToArray(head):
            arr = []
            while head:
                arr.append(head.val)
                head = head.next
            return arr
        def dfs(left, right):
            if left > right:
                return None
            mid = left + (right - left ) //2
            root = TreeNode(arr[mid])
            root.left = dfs(left, mid -1)
            root.right = dfs(mid + 1, right)
            return root
        arr = convertToArray(head)
        return dfs(0, len(arr) -1)