""" https://leetcode.com/problems/partition-list/
Given a linked list and a value x,
partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""


"""

建一个dummy
把小的都连到dummy上，把剩下都也连上
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
    def partition(self, head, x):
        dummy_small = ListNode(-1)
        dummy_large = ListNode(-1)

        small = dummy_small
        large = dummy_large

        while head:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                large.next = head
                large= large.next
            head = head.next

        small.next = dummy_large.next
        large.next = None

        return dummy_small.next


if __name__ == "__main__":
    head = ListNode(1)
    head.next = ListNode(4)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(5)
    head.next.next.next.next.next = ListNode(2)
    print (Solution().partition(head, 3))