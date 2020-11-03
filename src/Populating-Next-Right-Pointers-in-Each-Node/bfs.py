#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to populate next right pointers in each node. 
 '''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        bfs = [root]

        while bfs:
            new = []
            for i in range(len(bfs)):
                if bfs[i].left:
                    new.append(bfs[i].left)
                    new.append(bfs[i].right)

                if i == len(bfs) - 1:
                    bfs[i].next = None
                    continue

                bfs[i].next = bfs[i+1]

            bfs = new

        return root
