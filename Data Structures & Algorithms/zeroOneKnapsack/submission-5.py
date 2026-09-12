class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit)
        dic={}
        def dp(i,j):
            if j<=0: return 0
            if i>=n: return 0
            if (i,j) in dic: return dic[(i,j)]
            res=dp(i+1,j)
            if j-weight[i]>=0:
                res=max(res,profit[i]+dp(i+1,j-weight[i]))
            dic[(i,j)]=res
            return res
        return dp(0,capacity)