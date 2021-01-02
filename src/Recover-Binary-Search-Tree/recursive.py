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
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """

        def helper(root):
            global x, y, pred
            if not root:
                return
            helper(root.left)
            if pred and pred.val > root.val:
                y = root
                if x == -1:
                    x = pred
            pred = root
            helper(root.right)

        global x, y, pred
        x, y, pred = -1, -1, None

        helper(root)
        x.val, y.val = y.val, x.val
