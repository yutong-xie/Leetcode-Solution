#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Iteratively reverse a linked list from position m to n.
 '''


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """


        prev = None
        curr = head

        count = 0

        while count <= n:
            count += 1
            if count < m:
                prev = curr
                curr = curr.next

            elif count >= m and count <= n:
                if count == m:
                    mark = prev
                    end = curr
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp


        if mark:
            mark.next = prev
        else:
            head = prev

        end.next = curr


        return head
