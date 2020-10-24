#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to find the sum of deepest leaves.
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        bfs = [(root, 0)]
        visited = [(root,0)]
        max_deep = 0
        while bfs:
            new_bfs = []
            for i in bfs:
                node, cur_deep = i
                if not node.left and not node.right:
                    continue
                if node.left:
                    new_bfs.append((node.left, cur_deep+1))
                if node.right:
                    new_bfs.append((node.right, cur_deep+1))
                max_deep = max(cur_deep+1, max_deep)
            bfs = new_bfs
            visited += bfs


        ans = 0
        for i in visited:
            node, deep = i
            if deep == max_deep:
                ans += node.val

        return ans
