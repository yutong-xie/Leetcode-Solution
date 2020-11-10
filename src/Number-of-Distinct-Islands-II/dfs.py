#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dfs with shape transform to find number of distinct island.
 '''

class Solution(object):
    def numDistinctIslands2(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return 0

        R, C = len(grid), len(grid[0])

        shapes = set()

        def dfs(r, c):
            shape = []
            stack = [(r, c)]

            grid[r][c] = 0

            while stack:
                r, c = stack.pop()
                shape.append((r, c))
                for ir, ic in [(-1, 0),(1, 0),(0, 1),(0, -1)]:
                    if 0 <= r+ir < R and 0<= c+ic < C and grid[r+ir][c+ic]:
                        grid[r+ir][c+ic] = 0
                        stack.append((r+ir, c+ic))

            return transform(shape)

        def transform(shape):
            shape = sorted(shape)
            min_r, min_c = shape[0]

            return tuple([(r-min_r, c-min_c) for r, c in shape])



        def allshape(shape):
            shapes.add(shape)
            shapes.add(transform([(-r, c) for r, c in shape]))
            shapes.add(transform([(r, -c) for r, c in shape]))
            shapes.add(transform([(-r, -c) for r, c in shape]))
            shapes.add(transform([(c, r) for r, c in shape]))
            shapes.add(transform([(c, -r) for r, c in shape]))
            shapes.add(transform([(-c, r) for r, c in shape]))
            shapes.add(transform([(-c, -r) for r, c in shape]))

        ans = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    shape = dfs(r, c)
                    if shape not in shapes:
                        allshape(shape)
                        ans += 1
        return ans
