#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to find shortestPath in a grid with obstacles elimination.
 '''

class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not len(grid) or not len(grid[0]):
            return -1

        import collections
        ans = float("inf")

        R, C = len(grid), len(grid[0])

        # r, c, num_obstacle, step
        bfs = collections.deque([(0, 0, 0, 0)])

        visited = {(0,0,0)}

        while bfs:
            r, c, obs, step = bfs.popleft()

            if r == R-1 and c == C-1:
                return step

            for ir, ic in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + ir, c + ic
                if 0 <= nr < R and 0 <= nc < C:
                    new_obs = obs + grid[nr][nc]
                    if new_obs <= k and (nr, nc, new_obs) not in visited:
                        bfs.append((nr, nc, new_obs, step+1))
                        visited.add((nr, nc, new_obs))

        return -1
