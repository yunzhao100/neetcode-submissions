class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dic={}
        n=len(prices)
        def dp(i):
            if i in dic: return dic[i]
            if i>=n-1: return 0
            res=0
            res=dp(i+1)
            for j in range(i+1,n):
                if prices[j]>prices[i]:
                    res=max(res,prices[j]-prices[i]+dp(j+2))
            dic[i]=res
            return res
        return dp(0)