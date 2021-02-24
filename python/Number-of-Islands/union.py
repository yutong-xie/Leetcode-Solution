#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Union Find to calculate the number of islands.
 '''


class UnionFind:
    def __init__(self, grid):
        self.count = 0
        R,C = len(grid), len(grid[0])
        self.parent = [-1]*(R*C)
        self.rank = [0]*(R*C)


        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    self.parent[r*C+c] = r*C+c
                    self.count += 1

    def find(self,x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self,x,y):
        rootx = self.find(x)
        rooty = self.find(y)

        if (rootx != rooty):
            if (self.rank[rootx] < self.rank[rooty]):
                self.parent[rootx] = rooty
            elif (self.rank[rootx] > self.rank[rooty]):
                self.parent[rooty] = rootx
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def getCount(self):
        return self.count


class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        if grid == []:
            return 0

        uf = UnionFind(grid)
        R,C = len(grid), len(grid[0])

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    grid[r][c] = '0'
                    if (r-1 >= 0) and grid[r-1][c] == '1': uf.union(r*C+c, (r-1)*C+c)
                    if (r+1  < R) and grid[r+1][c] == '1': uf.union(r*C+c, (r+1)*C+c)
                    if (c-1 >= 0) and grid[r][c-1] == '1': uf.union(r*C+c, r*C+c-1)
                    if (c+1 < C) and grid[r][c+1] == '1': uf.union(r*C+c, r*C+c+1)

        return uf.getCount()
