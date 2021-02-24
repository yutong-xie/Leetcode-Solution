#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration to do inorder traversal of a binary tree
 '''

 # Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
 class Solution(object):
     def inorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """

         stack = []
         inorder = []
         while root:
             stack.append(root)
             root = root.left

         while stack or root:

             while root:
                 stack.append(root)
                 root = root.left


             root = stack.pop()
             inorder.append(root.val)
             root = root.right

         return inorder
