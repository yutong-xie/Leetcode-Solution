#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to find Zigzag level order traversal of a binary tree.
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        bfs = [root]
        ans = [[root.val]]
        reverse = True
        while bfs:
            new_bfs = []
            tmp = []
            for i in bfs:
                if i.left:
                    new_bfs.append(i.left)
                    tmp.append(i.left.val)
                if i.right:
                    new_bfs.append(i.right)
                    tmp.append(i.right.val)
            if not tmp:
                break
            if reverse:
                ans.append(tmp[::-1])
                reverse = False
            else:
                ans.append(tmp)
                reverse = True
            bfs = new_bfs

        return ans
