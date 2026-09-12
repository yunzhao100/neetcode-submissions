class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dic={}
        def dp(i):
            if i in dic: return dic[i]
            if i>=n: return 0
            res=cost[i]+min(dp(i+1),dp(i+2))
            dic[i]=res
            return res
        return min(dp(0),dp(1))