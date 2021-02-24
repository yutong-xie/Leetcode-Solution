#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to postorder traversal a binary tree.
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

        ans = []

        def helper(root):
            if not root:
                return
            if root.left:
                helper(root.left)
            if root.right:
                helper(root.right)
            ans.append(root.val)

        helper(root)
        return ans
