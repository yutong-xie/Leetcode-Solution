#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion version of DFS to solve the problem.
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

        def dfs(path, node):
            if node:
                path += str(node.val)
                if not node.left and not node.right:
                    ans.append(path)
                else:
                    path += "->"
                    dfs(path, node.left)
                    dfs(path, node.right)

        dfs("", root)

        return ans
