#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using backtracking to solve binary watch problem
 '''

class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """

        LED = [1,2,4,8,1,2,4,8,16,32]


        result = []

        def backtracking(count, hours, minutes, index):
            if hours > 11 or minutes > 59:
                return
            if count == 0:
                time = str(hours) + ":" + "0"*(minutes<10) + str(minutes)
                result.append(time)
                return

            if index < len(LED):
                # LED for hours on
                if index <= 3:
                    backtracking(count-1, hours+LED[index], minutes, index+1)
                # LED for minutes on
                else:
                    backtracking(count-1, hours, minutes+LED[index], index+1)

                backtracking(count, hours, minutes, index+1)

        backtracking(num, 0,0,0)

        return result
