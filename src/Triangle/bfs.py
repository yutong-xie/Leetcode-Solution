#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to find minimum path in a triangle.
 '''

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0

        l = len(triangle)

        top = triangle[0][0]
        bfs = [(0, 0, top)]
        ans = float("inf")
        level = 0



        while bfs:
            level += 1
            new_bfs = {}
            for r, c, cost in bfs:
                if level == l:
                    ans = min(ans, cost)
                    continue
                for ir, ic in [(1, 0), (1, 1)]:
                    if r + ir < l:
                        new_cost = cost + triangle[r+ir][c+ic]
                        if (r+ir, c+ic) not in new_bfs:
                            new_bfs[(r+ir, c+ic)] = new_cost
                        else:
                            new_bfs[(r+ir, c+ic)] = min(new_bfs[(r+ir, c+ic)], new_cost)



            bfs = []
            for r, c in new_bfs:
                bfs.append((r, c, new_bfs[(r,c)]))

        return ans
