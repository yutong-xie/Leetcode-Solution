#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using greedy algorithm verison topological sort to solve course schedule problem
 '''

def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        indegree = [0]*numCourses
        graph = [[] for i in range(numCourses)]
        stack = []
        result = []

        for y,x in prerequisites:
            indegree[y] += 1
            graph[x].append(y)


        for i in range(len(indegree)):
            if indegree[i] == 0:
                stack.append(i)

        while len(stack) != 0:
            v = stack.pop()
            result.append(v)
            for i in graph[v]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    stack.append(i)

        return True if len(result) == numCourses else False numCourses else False
