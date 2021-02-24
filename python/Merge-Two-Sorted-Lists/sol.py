#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration two merge two sorted linked list
 '''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = ListNode()
        head = root

        while l1 and l2:
            if l1.val <= l2.val:
                head.next = l1
                l1 = l1.next
                head = head.next
            else:
                head.next = l2
                l2 = l2.next
                head = head.next
        if l1:
            head.next = l1
        else:
            head.next = l2

        return root.next
