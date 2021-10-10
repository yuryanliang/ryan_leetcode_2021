""" https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Given a linked list, remove the nth node from the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end, the linked list becomes 1->2->3->5.

"""
"""先统计链表的数字的个数，然后删除第len-n个数"""

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None

class Sol:
    def remove_n(self, head, n):
        #1. count length
        length = 0
        cur = head

        while cur:
            length += 1
            cur = cur.next
        #2. remove node
        dummy = ListNode(-1)
        dummy.next = head

        pointer = dummy
        for i in range(length - n):
             pointer = pointer.next

        pointer.next = pointer.next.next
        return dummy.next