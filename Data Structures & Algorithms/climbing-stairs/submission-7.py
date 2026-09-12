class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[-1]*(n+1)
        def dfs(n):
            if n<=2:
                return n
            if memo[n]!=-1:
                return memo[n]
            memo[n]=dfs(n-1)+dfs(n-2)
            return memo[n]
        return dfs(n)