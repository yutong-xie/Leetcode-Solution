#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to construct binary tree from postorder and inorder traversal
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
global post_index

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        hashmap = {}
        for i, val in enumerate(inorder):
            hashmap[val] = i

        global post_index
        post_index = len(inorder)-1

        def helper(left_index, right_index):
            if left_index >= right_index:
                return None

            global post_index

            root_val = postorder[post_index]
            root = TreeNode(root_val)

            post_index -= 1

            index = hashmap[root_val]

            root.right = helper(index+1, right_index)
            root.left = helper(left_index, index)

            return root

        return helper(0, len(inorder))
