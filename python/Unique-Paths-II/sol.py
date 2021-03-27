class Solution(object):
    def uniquePathsWithObstacles(self, grid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(n):
            if grid[0][i] == 1: 
                break
            dp[0][i]  = 1
            
        for i in range(m):
            if grid[i][0] == 1:
                break
            dp[i][0] = 1 
            
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] != 1:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[-1][-1]