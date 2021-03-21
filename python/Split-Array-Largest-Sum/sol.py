class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        l = max(nums)
        r = sum(nums)
        
        ans = r
        while l <= r :
            mid = (l+r)//2
            sum_cur = 0 
            num = 1
            for i in range(len(nums)):
                if (sum_cur + nums[i] > mid):
                    sum_cur = nums[i]
                    num += 1
                else:
                    sum_cur += nums[i]
            if num <= m:
                ans = min(ans, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return ans
        
                    
                