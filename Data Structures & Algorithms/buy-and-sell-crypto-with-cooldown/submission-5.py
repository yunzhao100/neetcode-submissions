class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dic={}
        def dp(i,holding):
            if i>=n: return 0
            if (i,holding) in dic: return dic[(i,holding)]
            res=dp(i+1,holding)
            if holding:
                res=max(res,prices[i]+dp(i+2,False))
            else:
                res=max(res,-prices[i]+dp(i+1,True))
            dic[(i,holding)]=res
            return res
        return dp(0,False)