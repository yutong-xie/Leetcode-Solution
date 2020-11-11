#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to find max area of island
 '''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        R, C = len(grid), len(grid[0])

        if not R or not C:
            return 0

        def bfs(r, c):

            area = 0
            visited = {(r,c)}
            bfs = collections.deque([(r,c)])
            while bfs:
                r, c = bfs.popleft()
                grid[r][c] = 0
                area += 1
                for ir, ic in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if 0 <= r+ir < R and 0 <= c+ic < C and grid[r+ir][c+ic]:
                        if (r+ir, c+ic) not in visited:
                            visited.add((r+ir, c+ic))
                            bfs.append((r+ir, c+ic))

            return area

        ans = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    area = bfs(r, c)
                    ans = max(ans, area)

        return ans
