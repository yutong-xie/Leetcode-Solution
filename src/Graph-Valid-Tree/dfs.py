#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using DFS to judge whether undirected graph is a valid tree
 '''

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n-1:
            return False


        import collections

        graph = collections.defaultdict(list)

        for edge in edges:
            n1, n2 = edge
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = {0}
        stack = [0]

        while stack:
            node = stack.pop()
            for adj in graph[node]:
                if adj in visited:
                    continue
                else:
                    visited.add(adj)
                    stack.append(adj)

        return len(visited) == n
