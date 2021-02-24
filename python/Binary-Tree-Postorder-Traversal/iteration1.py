#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration to postorder traversal a binary tree.
    #### Method ####  
      1. Find root -> right -> left first
      2. Reverse the answer
 '''

 # Definition for a binary tree node.
 # class TreeNode(object):
 #     def __init__(self, val=0, left=None, right=None):
 #         self.val = val
 #         self.left = left
 #         self.right = right
 class Solution(object):
     def postorderTraversal(self, root):
         """
         :type root: TreeNode
         :rtype: List[int]
         """

         if not root:
             return []

         ans = []

         stack = [root]
         while stack:
             curr = stack.pop()
             ans.append(curr.val)
             if curr.left:
                 stack.append(curr.left)
             if curr.right:
                 stack.append(curr.right)

         return ans[::-1]
