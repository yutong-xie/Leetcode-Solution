class Solution(object):
    def missingNumber(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if arr[0] > arr[1]:
            arr = arr[::-1]
        
        interval = (arr[-1] - arr[0]) // len(arr)
        l, r = 0, len(arr) - 1
        while l < r: 
            mid = (l+r)//2 
            if arr[mid] == arr[0] + interval * mid:
                l = mid + 1
            else:
                r = mid
        
        return arr[0] + l * interval