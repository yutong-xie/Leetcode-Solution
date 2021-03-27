class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n, m = len(word1), len(word2)
        if n * m == 0:
            return n + m
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(m+1):
            dp[i][0] = i
        for i in range(n+1):
            dp[0][i] = i 
        
        for i in range(1, m+1): 
            for j in range(1, n+1):
                left = dp[i][j-1] + 1
                down = dp[i-1][j] + 1
                left_down = dp[i-1][j-1]
                
                if word1[j-1] != word2[i-1]:
                    left_down += 1
                dp[i][j] = min(left, down, left_down)
        
        return dp[-1][-1]
                    