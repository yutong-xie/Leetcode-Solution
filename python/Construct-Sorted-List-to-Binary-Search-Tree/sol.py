#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using binary search to convert sorted list to binary search tree.
 '''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        array = []

        while head:
            array.append(head.val)
            head = head.next

        def helper(l,r):
            if l > r:
                return None

            mid = (l+r) // 2
            root = TreeNode(array[mid])

            root.left = helper(l, mid-1)
            root.right = helper(mid+1, r)

            return root


        root = helper(0, len(array)-1)

        return root
