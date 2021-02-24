#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using DFS with memorization to find cheapest flights within K stops.

    The number of recursive calls we can potentially make is O(VK).
    In each recursive call, we iterate over a given node's neighbors.
    That takes time O(V) because we are using an adjacency matrix.
    Thus, the overall time complexity is O(V^2⋅K).

 '''

class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        import collections
        airmap = collections.defaultdict(list)
        costs = collections.defaultdict(int)

        for e in flights:
            start, end, cost = e
            airmap[start].append((end, cost))

        visited = {}


        def dfs(node, stops):
            if node == dst:
                return 0

            if stops < 0:
                return float("inf")

            if (node, stops) in visited:
                return visited[(node, stops)]

            ans = float("inf")
            for adj, cost in airmap[node]:
                ans = min(ans, dfs(adj, stops-1) + cost)

            visited[(node, stops)] = ans
            return ans

        output = dfs(src, K)

        return output if output != float("inf") else -1
