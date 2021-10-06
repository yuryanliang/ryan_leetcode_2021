""" https://leetcode.com/problems/remove-duplicates-from-sorted-list/
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Sol:
    def iteration(self, head):
        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head

        while head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        return dummy.next
    def recursion(self, head):
        if not head or not head.next:
            return head
        h = self.recursion(head.next)
        if head.val != h.val:
            head.next = h
        else:
            head.next = h.next
        return head
