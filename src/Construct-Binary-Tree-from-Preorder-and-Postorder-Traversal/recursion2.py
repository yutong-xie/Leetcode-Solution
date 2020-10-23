#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to construct binary tree from preorder and postorder traversal.
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        def helper(pre_index, post_index, N):
            if N == 0:
                return None

            root = TreeNode(pre[pre_index])

            if N == 1 :
                return root

            curr_pre = pre[pre_index:pre_index+N]
            curr_post = post[post_index:post_index+N]

            # Assume the left branch of root has L nodes
            left_val = curr_pre[1]
            L = curr_post.index(left_val) + 1

                    "

            root.left = helper(pre_index+1, post_index, L)
            root.right = helper(pre_index+L+1, post_index+L, N-L-1)

            return root

        return helper(0, 0, len(pre))
