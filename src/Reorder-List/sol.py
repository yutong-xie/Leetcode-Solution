#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Split the linkedlist to two parts, reverse the second part and merge two linkedlist to reorder linkedlist.
 '''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow

        prev, curr = None, mid

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        left, right = head, prev

        while right.next:
            tmp = left.next
            left.next = right
            left = tmp

            tmp = right.next
            right.next = left
            right = tmp

#             left.next, left = right, left.next
#             right.next, right = left, right.next
