#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Find idle time to realize task scheduler.
 '''

class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        import collections
        count = collections.Counter(tasks)

        sort_count = sorted(count.items(), key = lambda x: -x[1])

        idle_time = (sort_count[0][1] - 1) * n

        for i in range(1, len(sort_count)):
            if idle_time < 0:
                break
            idle_time -= min(sort_count[0][1] - 1, sort_count[i][1])

        idle_time = max(0, idle_time)

        return len(tasks) + idle_time
