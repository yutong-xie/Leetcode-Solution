#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using greedy algorithm verison topological sort to solve sequence reconstruction problem
 '''


from collections import defaultdict
class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """

        # indegree = defaultdict(int)
        # graph = defaultdict(list)
        indegree = {k: 0 for seq in seqs for k in seq}
        graph = {x: [] for seq in seqs for x in seq}


        for pair in seqs:

            for i in range(len(pair)-1):
                x, y = pair[i], pair[i+1]
                graph[x].append(y)
                indegree[y] += 1
                indegree[x] += 0

        # if indegree and org have different length, org must be invalid
        if len(indegree) != len(org):

            return False

        stack = []
        result = []
        for i in indegree:
            if indegree[i] == 0:
                stack.append(i)

        while len(stack) != 0:
            # if there exists more than one 0 indegree node, the path will be not unique.
            if len(stack) > 1:
                return False

            v = stack.pop()
            result.append(v)
            for adj in graph[v]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    stack.append(adj)

        return result == org
