#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration to search node in BST
 '''

 # Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
 class Solution(object):
     def searchBST(self, root, val):
         """
         :type root: TreeNode
         :type val: int
         :rtype: TreeNode
         """
         while root:
             if root.val == val:
                 return root
             elif root.val < val:
                 root = root.right
             else:
                 root = root.left

         return None
