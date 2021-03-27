class Solution(object):
    def fixedPoint(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        l, r = 0, len(arr) - 1 
        ans = []
        result = -1
        
        while l <= r: 
            mid = (l+r) // 2
            if arr[mid] == mid:
                result = mid
                r = mid - 1
            elif arr[mid] < mid:
                l = mid + 1 
            else:
                r = mid - 1
        
        return result
                
        