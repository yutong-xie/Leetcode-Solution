#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using Dynamic Programming to solve minimum number of days to eat n oranges
 '''

import collections
class Solution(object):
    def minDays(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {n: 0}
        queue = collections.deque()
        queue.append(n)

        while queue:
            num = queue.pop()
            new_num = num // 2
            if num == 1:
                new_days = dp[num] + 1
            else:
                new_days = dp[num] + 1 + num % 2
            if new_num not in dp or new_days < dp[new_num]:
                dp[new_num] = new_days
                if new_num not in queue:
                    queue.append(new_num)

            new_num = num // 3 
            if num == 1:
                new_days = dp[num] + 1
            else:
                new_days = dp[num] + 1 + num % 3
            if new_num not in dp or new_days < dp[new_num]:
                dp[new_num] = new_days
                if new_num not in queue:
                    queue.append(new_num)

        return dp[0]
