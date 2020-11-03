#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to merge two BST.
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        root = t1

        def helper(t1, t2):
            if not t1 and not t2:
                return None

            if t1 and not t2:
                return t1

            if t2 and not t1:
                return t2

            if t1 and t2:
                t1.val = t1.val + t2.val
                t1.left = helper(t1.left, t2.left)
                t1.right = helper(t1.right, t2.right)

            return t1

        return helper(t1, t2)
