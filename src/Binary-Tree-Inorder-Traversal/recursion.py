#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to do inorder traversal of a binary tree
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

        def helper(root, stack):
            if root != None:
                helper(root.left, stack)
                stack.append(root.val)
                helper(root.right, stack)

        helper(root, stack)

        return stack
