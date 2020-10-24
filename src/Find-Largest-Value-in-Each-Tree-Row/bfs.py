#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to find larget value in each tree row.
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        bfs = [root]
        ans = [root.val]

        while bfs:
            new_bfs = []
            cur_val = float("-inf")
            for node in bfs:
                if node.left:
                    cur_val = max(cur_val, node.left.val)
                    new_bfs.append(node.left)
                if node.right:
                    cur_val = max(cur_val, node.right.val)
                    new_bfs.append(node.right)

            bfs = new_bfs

            if bfs: ans.append(cur_val)

        return ans
