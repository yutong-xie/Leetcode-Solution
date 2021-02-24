#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using dfs algorithm verison topological sort to solve course schedule problem
 '''


from collections import defaultdict
class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # for status, 0 means not visited, 1 means visited during dfs search, 2 means visited in main function
        graph = defaultdict(list)
        status = {i: 0 for i in range(numCourses)}
        result = []

        global possible
        possible = True

        for y,x in prerequisites:
            graph[x].append(y)

        def dfs_improve(v):
            global possible

            if not possible:
                return

            # Start recursion
            status[v] = 1

            for i in graph[v]:
                # if never visited, continue recursion
                if status[i] == 0:
                    dfs_improve(i)
                # if the node alread visited in current recursion, it means that there exists loop.
                elif status[i] == 1:
                     possible = False

            status[v] = 2
            result.append(v)

        for v in range(numCourses):
            if status[v] == 0:
                dfs_improve(v)

        return result[::-1] if possible else []
