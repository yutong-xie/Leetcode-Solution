#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2021, Yutong Xie, UIUC.
    Using backtracking to find the solution of a sudoku.
 '''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        global solved
        solved = False

        def valid(d, i, j):
            if d in board[i]:
                return False
            for row in range(9):
                if d == board[row][j]:
                    return False
            col_start, col_end = (j//3)*3, (j//3)*3+3
            row_start, row_end = (i//3)*3, (i//3)*3+3
            for col in range(col_start, col_end):
                for row in range(row_start, row_end):
                    if d == board[row][col]:
                        return False
            return True

        def placenext(i, j):
            global solved
            if i == 8 and j == 8:
                solved = True
            else:
                if j != 8:
                    helper(i, j+1)
                else:
                    helper(i+1, 0)

        def helper(i, j):
            global solved
            if board[i][j] != ".":
                placenext(i, j)
            else:
                for num in "123456789":
                    if valid(num, i, j):
                        board[i][j] = num
                        placenext(i, j)
                    if not solved:
                        board[i][j] = "."
        helper(0,0)
