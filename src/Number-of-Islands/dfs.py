#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using DFS to calculate the number of islands.
 '''

 class Solution(object):
     def numIslands(self, grid):
         """
         :type grid: List[List[str]]
         :rtype: int
         """

         def dfs(grid,r,c):
             R = len(grid)
             C = len(grid[0])
             grid[r][c] = '0'

             if (r-1 >= 0) and grid[r-1][c] == '1': dfs(grid, r-1, c)
             if (r+1 < R) and grid[r+1][c] == '1': dfs(grid, r+1, c)
             if (c-1 >= 0) and grid[r][c-1] == '1': dfs(grid, r, c-1)
             if (c+1 < C) and grid[r][c+1] == '1': dfs(grid, r, c+1)


         if grid == []:
             return 0

         ans = 0
         for r in range(len(grid)):
             for c in range(len(grid[0])):
                 if grid[r][c] == '1':
                     ans += 1
                     dfs(grid, r, c)

         return ans
