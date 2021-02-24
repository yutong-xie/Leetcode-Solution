#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Find the entrance of the circle in linked-list using two pointers.
 '''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def hasCycle():
            slow, fast = head, head

            while fast != None and fast.next != None:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return slow

            return None

        intersect = hasCycle()

        if intersect == None:
            return None
        else:
            p1, p2 = head, intersect
            while p1 != p2:
                p1 = p1.next
                p2 = p2.next

            return p1


        
