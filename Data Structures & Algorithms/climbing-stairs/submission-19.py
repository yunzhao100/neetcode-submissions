class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[-1]*n
        def dfs(i):
            if memo[i]!=-1:
                return memo[i]
            if i==n-1:
                memo[i]=1
            elif i==n-2:
                memo[i]=2
            else:
                memo[i]=dfs(i+1)+dfs(i+2)
            return memo[i]
        return dfs(0)