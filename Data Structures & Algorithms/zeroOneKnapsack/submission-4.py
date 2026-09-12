class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit)
        dic={}
        def dp(i,j):
            if (i,j) in dic: return dic[(i,j)]
            if i>=n or j<0: return 0
            res=dp(i+1,j)
            remaining_capacity=j-weight[i]
            if remaining_capacity>=0:
                res=max(res,profit[i]+dp(i+1,remaining_capacity))
            dic[(i,j)]=res
            return res
        return dp(0,capacity)