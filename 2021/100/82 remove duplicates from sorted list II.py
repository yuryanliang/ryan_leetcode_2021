""" https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.



Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]


Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
"""
class Solution:
    def deleteDuplicates(self, head):
        dummy = ListNode(-1)
        dummy.next = head
        prev = dummy
        curr = dummy.next

        while curr:
            if curr.next and curr.val == curr.next.val:
                val_to_remove = curr.val
                while curr and curr.val == val_to_remove:
                    curr = curr.next
                prev.next = curr

            else:
                prev, curr = curr, curr.next
        return dummy.next

