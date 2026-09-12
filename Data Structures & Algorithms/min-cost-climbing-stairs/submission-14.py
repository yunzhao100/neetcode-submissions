class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dic={n-1:cost[-1],n-2:cost[-2]}
        def dp(i):
            if i in dic: return dic[i]
            dic[i]=cost[i]+min(dp(i+1),dp(i+2))
            return dic[i]
        return min(dp(0),dp(1))