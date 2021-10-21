""" https://leetcode.com/problems/reverse-linked-list-ii/
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

"""
先前进到 m-1位， 
然后翻转 m-n次
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        if self:
            return "{} -> {}".format(self.val, repr(self.next))

class Solution:
    def reverseBetween(self, head, m, n):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        for i in range(m -1): # go forward m
            pre = pre.next

        cur = pre.next # cur is at m node

        for i in range(m, n):
            after = cur.next # define after

            # reverse cur and after
            cur.next = after.next # set cur.next
            after.next = pre.next # set after.next
            pre.next = after
        return dummy.next

# Iterative solution.
class Sol:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        dummy = ListNode(float("-inf"))
        while head:
            dummy.next, head.next, head = head, dummy.next, head.next
        return dummy.next

if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    print (Solution().reverseBetween(head, 2, 4))