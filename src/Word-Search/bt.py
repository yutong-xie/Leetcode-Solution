#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using back tracking to solve word search problem
 '''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return False

        w, h = len(board[0]), len(board)


        def helper(row, col, word):

            if word == "":
                return True

            if row < 0 or row >= h or col < 0 or col >= w or board[row][col] != word[0]:
                return False

            board[row][col] = "*"
            ret = False

            for x, y in [(0,1), (0,-1), (1,0), (-1,0)]:
                ret = helper(row+x, col+y, word[1:])
                if ret:
                    break
            board[row][col] = word[0]

            return ret

        for i in range(w):
            for j in range(h):
                if helper(j, i, word):
                    return True

        return False
