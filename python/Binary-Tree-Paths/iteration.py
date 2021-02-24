#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using iteration version of DFS to solve the problem. 
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        ans = []

        stack = [(root, str(root.val))]

        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                ans.append(path)
            if node.left:
                stack.append((node.left, path+"->"+str(node.left.val)))
            if node.right:
                stack.append((node.right, path+"->"+str(node.right.val)))

        return ans
