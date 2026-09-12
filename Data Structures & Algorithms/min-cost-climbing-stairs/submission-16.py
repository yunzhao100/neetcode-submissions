class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dic={}
        n=len(cost)
        def dp(i):
            if i>=n: return 0
            if i in dic: return dic[i]
            res=min(cost[i]+dp(i+1),cost[i]+dp(i+2))
            dic[i]=res
            return res
        return min(dp(0),dp(1))