class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        memo=[-1]*n
        def dp(i):
            if memo[i]!=-1:
                return memo[i]
            if i==n-1:
                memo[i]=cost[i]
            elif i==n-2:
                memo[i]=cost[i]
            else:
                memo[i]=cost[i]+min(dp(i+1),dp(i+2))
            return memo[i]
        return min(dp(0),dp(1))