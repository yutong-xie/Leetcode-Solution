#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Using dictionary to valid the sudoku.
 '''

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        from collections import defaultdict
        row = [defaultdict(int) for i in range(9)]
        col = [defaultdict(int) for i in range(9)]
        box = [defaultdict(int) for i in range(9)]

        for r in range(9):
            for c in range(9):
                box_index = (r//3)*3 + c//3
                num = board[r][c]
                if num != '.':
                    row[r][num] += 1
                    col[c][num] += 1
                    box[box_index][num] += 1

                if row[r][num] > 1 or col[c][num] > 1 or box[box_index][num] > 1:
                    return False
                    
        return True
