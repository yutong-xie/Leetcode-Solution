#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using deque and inorder traversal to solve
 '''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.inorder = deque()

        while self.stack or root:
            while root:
                self.stack.append(root)
                root = root.left

            root = self.stack.pop()
            self.inorder.append(root.val)
            root = root.right



    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        return self.inorder.popleft()

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.inorder) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
