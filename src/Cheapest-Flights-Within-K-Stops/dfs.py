#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using DFS with memorization to find cheapest flights within K stops.
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
            airmap[start].append(end)
            costs[(start, end)] = cost

        visited = {}


        def dfs(node, stops):
            if node == dst:
                return 0

            if stops < 0:
                return float("inf")

            if (node, stops) in visited:
                return visited[(node, stops)]

            ans = float("inf")
            for adj in airmap[node]:
                ans = min(ans, dfs(adj, stops-1) + costs[(node, adj)])

            visited[(node, stops)] = ans
            return ans

        output = dfs(src, K)

        return output if output != float("inf") else -1
