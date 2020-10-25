#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using bfs to solve the maze problem.
 '''

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        R = len(maze)
        C = len(maze[0])


        bfs = [start]
        visited = [[0 for _ in range(C)] for _ in range(R)]
        visited[start[0]][start[1]] = 1
        d = [(0,1),(0,-1),(1,0),(-1,0)]
        while bfs:
            new_bfs = []
            for node in bfs:
                if node == destination:
                    return True
                for ir, ic in d:
                    r = node[0] + ir
                    c = node[1] + ic
                    while 0 <= r < R and 0 <= c < C and maze[r][c] == 0:
                        r += ir
                        c += ic

                    if visited[r-ir][c-ic] == 0:
                        new_bfs.append([r-ir, c-ic])
                        visited[r-ir][c-ic] = 1
            bfs = new_bfs

        return False
