#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using topological sort to solve alien dictionary problem
 '''

class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        from collections import defaultdict

        if len(words) == 1:
            return words[0]

        indegree = defaultdict(int)
        graph = defaultdict(list)

        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i+1]
            for w in w1:
                indegree[w] += 0
            for w in w2:
                indegree[w] += 0
            L = min(len(w1), len(w2))
            for j in range(L):
                a1 = w1[j]
                a2 = w2[j]
                if a1 != a2:
                    if a2 not in graph[a1]:
                        graph[a1].append(a2)
                        indegree[a2] += 1
                    break
            else:
                if len(w2) < len(w1): return ""

        stack = []
        ans = ""

        for i in indegree:
            if indegree[i] == 0:
                stack.append(i)

        while stack:
            w = stack.pop()
            ans += w

            for adj in graph[w]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    stack.append(adj)

        return ans if len(ans) == len(indegree) else ""
