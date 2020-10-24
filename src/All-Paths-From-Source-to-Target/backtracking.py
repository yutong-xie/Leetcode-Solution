#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using backtracking to find all paths from source to target.
 '''

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """


        paths = []
        n = len(graph)

        def dfs(node, path):
            if node == n-1:
                paths.append(path)
                return
            for adj in graph[node]:
                dfs(adj, path+[adj])

        dfs(0, [0])

        return paths
