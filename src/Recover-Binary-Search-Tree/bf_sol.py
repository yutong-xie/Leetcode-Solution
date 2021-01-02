#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using inorder traversal to recover wrong binary tree.
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        def inorder(r):
            if not r:
                return []
            return inorder(r.left) + [r.val] + inorder(r.right)

        def find_swap(lists):
            x, y = -1, -1
            for i in range(len(lists)-1):
                if lists[i] > lists[i+1]:
                    y = lists[i+1]
                    if x == -1:
                        x = lists[i]
                    else:
                        break

            return x, y

        def helper(r, count):
            if r:
                if r.val == x or r.val == y:
                    r.val = x if r.val == y else y
                    count -= 1
                    if count == 0:
                        return
                helper(r.left, count)
                helper(r.right, count)

        lists = inorder(root)
        x, y = find_swap(lists)
        helper(root, 2)
