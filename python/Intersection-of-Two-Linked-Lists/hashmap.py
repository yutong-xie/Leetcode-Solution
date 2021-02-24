#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashtable to find the intersection of two linked lists.
 '''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        hashtable = {}

        while headA:
            hashtable[headA] = 0
            headA = headA.next

        while headB:
            if headB in hashtable:
                return headB
            headB = headB.next

        return None
