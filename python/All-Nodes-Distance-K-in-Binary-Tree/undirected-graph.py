#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using undirected graph to find all nodes distance k in binary tree
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """

        if not root:
            return []

        # construct undirected map
        m = defaultdict(list)
        stack = [root]

        while stack:
            root = stack.pop()
            if not root:
                continue
            if root.left:
                m[root.val].append(root.left.val)
                m[root.left.val].append(root.val)
                stack.append(root.left)
            if root.right:
                m[root.val].append(root.right.val)
                m[root.right.val].append(root.val)
                stack.append(root.right)

        # bfs
        visited = {target.val}
        bfs = [target.val]

        while bfs:
            if K == 0:
                return bfs
            new_bfs = []
            for i in bfs:
                adj = m[i]
                for i in adj:
                    if i in visited:
                        continue
                    else:
                        visited.add(i)
                        new_bfs.append(i)
            bfs = new_bfs
            K -= 1

        return []
