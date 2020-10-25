#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
    Copyright 2020, Yutong Xie, UIUC.
    Using random index to shuffle an array
 '''

 class Solution(object):
   import copy
   import random
   def __init__(self, nums):
       """
       :type nums: List[int]
       """
       self.array = nums
       self.original = list(self.array)        # equal to deepcopy

   def reset(self):
       """
       Resets the array to its original configuration and return it.
       :rtype: List[int]
       """
       self.array = self.original
       self.original = list(self.original)
       return self.array

   def shuffle(self):
       """
       Returns a random shuffling of the array.
       :rtype: List[int]
       """
       l = len(self.array)
       for i in range(l):
           random_i = random.randrange(0,l)
           self.array[i], self.array[random_i] = self.array[random_i], self.array[i]

       return self.array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
