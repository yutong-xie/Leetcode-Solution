#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using heapq to merge k lists
 '''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        q = []

        head = ListNode()
        point = head

        for l in lists:
            if l:
                heapq.heappush(q, (l.val, l))

        while q:
            val, node = heapq.heappop(q)
            point.next = node
            point = point.next
            node = node.next
            if node:
                heapq.heappush(q, (node.val, node))

        return head.next
