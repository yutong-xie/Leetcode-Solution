#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using recursion to delete node in BST
 '''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # The functions to find successor and predecessor are based on the assumption that root has two children.
    def successor(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root
    def predecessor(self, root):
        root = root.left
        while root.right:
            root = root.right
        return root

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        # delete the current node
        else:
            # the node is a leaf
            if not root.left and not root.right:
                root = None
            # the node has two children
            elif root.right:
                successor = self.successor(root)
                root.val = successor.val
                root.right = self.deleteNode(root.right, root.val)
            # the node has only left child
            elif root.left:
                predecessor = self.predecessor(root)
                root.val = predecessor.val
                predecessor = None
                root.left = self.deleteNode(root.left, root.val)
        return root
