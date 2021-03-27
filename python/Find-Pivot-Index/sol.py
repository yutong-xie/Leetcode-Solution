class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix = [0]
        for i in nums:
            prefix.append(prefix[-1]+i)
            
        for i in range(len(nums)):
            if prefix[i] - prefix[0] == prefix[-1] - prefix[i+1]:
                return i
            
        return -1 