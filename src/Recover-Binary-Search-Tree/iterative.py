#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using inorder traversal to recover wrong binary tree.
 '''

 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, r):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        x, y, pred = -1, -1, None
        stack = []
        while r or stack:
            while r:
                stack.append(r)
                r = r.left
            r = stack.pop()
            if pred and pred.val > r.val:
                y = r
                if x == -1:
                    x = pred
            pred = r
            r = r.right

        x.val, y.val = y.val, x.val
