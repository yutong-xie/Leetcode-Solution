#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration to insert node into BST
 '''

 # Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
 class Solution(object):
     def insertIntoBST(self, root, val):
         """
         :type root: TreeNode
         :type val: int
         :rtype: TreeNode
         """

         current = root

         while current:
             if current.val > val:
                 if not current.left:
                     current.left = TreeNode(val)
                     return root
                 else:
                     current = current.left
             else:
                 if not current.right:
                     current.right = TreeNode(val)
                     return root
                 else:
                     current = current.right


         # if the tree is empty
         return TreeNode(val)
