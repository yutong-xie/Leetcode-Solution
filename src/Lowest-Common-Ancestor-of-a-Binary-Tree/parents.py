#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using parents pointer to find lowest common ancestor of two nodes
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        parents = {}
        parents[root] = None
        bfs = [root]
        while bfs:
            new_bfs = []
            for i in bfs:
                if i.left:
                    new_bfs.append(i.left)
                    parents[i.left] = i
                if i.right:
                    new_bfs.append(i.right)
                    parents[i.right] = i

            bfs = new_bfs

        p_parent = [p]

        while p:
            p_parent.append(parents[p])
            p = parents[p]

        while q:
            if q in p_parent:
                return q
            else:
                q = parents[q]
