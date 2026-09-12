class Solution:
    def climbStairs(self, n: int) -> int:
        cache=[-1]*n # how many ways to get to the final spot
        def dfs(i):
            if i>=n:
                return i==n 
                # if it is already at the final spot, the number of ways is counted as 1
                # if is is over the final spot, the number of ways is counted as 0
            if cache[i]!=-1:
                return cache[i]
            cache[i]=dfs(i+1)+dfs(i+2)
            return cache[i]
        return dfs(0)