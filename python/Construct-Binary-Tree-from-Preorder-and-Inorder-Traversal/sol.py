#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to construct binary tree from preorder and inorder traversal 
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
global pre_index
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        hashmap = {}
        for i in range(len(inorder)):
            hashmap[inorder[i]] = i

        global pre_index
        pre_index = 0

        def helper(left_index, right_index):

            if left_index >= right_index:
                return None

            global pre_index

            root_val = preorder[pre_index]
            root = TreeNode(root_val)

            index = hashmap[root_val]

            pre_index += 1

            root.left = helper(left_index, index)
            root.right = helper(index+1, right_index)

            return root

        return helper(0, len(inorder))
