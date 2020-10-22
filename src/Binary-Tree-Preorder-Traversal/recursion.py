#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to preorder traversal a binary tree. 
 '''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        ans = []

        def helper(node):
            if not node:
                return
            ans.append(node.val)
            if node.left:
                helper(node.left)
            if node.right:
                helper(node.right)

        helper(root)

        return ans
