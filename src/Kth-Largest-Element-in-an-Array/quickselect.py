#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using quick select to find kth largest element in an array.
 '''

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(l, r):
            pivot_index = random.randint(l, r)
            pivot = nums[pivot_index]

            nums[pivot_index], nums[r] = nums[r], nums[pivot_index]
            index = l

            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[index] = nums[index], nums[i]
                    index += 1

            nums[index], nums[r] = nums[r], nums[index]

            return index

        def select(l, r, index):
            if l == r:
                return nums[l]

            pivot_index = partition(l, r)

            if pivot_index == index:
                return nums[pivot_index]
            elif pivot_index < index:
                return select(pivot_index+1, r, index)
            else:
                return select(l, pivot_index-1, index)


        return select(0, len(nums)-1, len(nums)-k)
