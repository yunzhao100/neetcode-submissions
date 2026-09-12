class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dic={n-1:cost[n-1], n-2:cost[n-2]}
        def dp(i):
            if i>n:
                return 0
            # minimum cost from i to finish
            if i in dic:
                return dic[i]
            dic[i]=min(cost[i]+dp(i+1),cost[i]+dp(i+2))
            return dic[i]
        return min(dp(0),dp(1))