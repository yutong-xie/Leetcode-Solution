#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Valid the sudoku.
 '''


 class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def check(num, i, j):
            # check the same row
            for col in range(9):
                if board[i][col] == num and col != j:
                    return False
            # check the same column
            for row in range(9):
                if board[row][j] == num and row != i:
                    return False
            # check the 3x3 window
            col_start, col_end = (j//3)*3, (j//3)*3+3
            row_start, row_end = (i//3)*3, (i//3)*3+3
            for col in range(col_start, col_end):
                for row in range(row_start, row_end):
                    if board[row][col] == num:
                        if row != i or col != j:
                            return False
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not check(board[i][j], i, j):
                        return False

        return True
