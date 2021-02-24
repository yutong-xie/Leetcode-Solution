#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using hashmap to test whether a cycle exists in the linked list
 '''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        hashmap = {}

        while head:
            if head in hashmap:
                return True
            else:
                hashmap[head] = 0
                head = head.next

        return False
