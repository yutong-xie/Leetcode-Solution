#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration to postorder traversal a binary tree.
    Directly conduct the postorder traversal
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
       stack = []

       while stack or root:
           while root:
               if root.right:
                   stack.append(root.right)
               stack.append(root)
               root = root.left

           node = stack.pop()
           if stack and node.right == stack[-1]:
               stack[-1] = node
               root = node.right
           else:
               ans.append(node.val)

       return ans
