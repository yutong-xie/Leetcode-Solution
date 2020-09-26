#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using divide and conquer method to merge k lists
 '''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution(object):
    def merge2lists(self, l1, l2):
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

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        n = len(lists)
        if n == 0 :
            return None
        interval = 1
        while interval < n:
            for i in range(0, n-interval, interval*2):
                lists[i] = self.merge2lists(lists[i], lists[i+interval])
            interval *= 2

        return lists[0]
