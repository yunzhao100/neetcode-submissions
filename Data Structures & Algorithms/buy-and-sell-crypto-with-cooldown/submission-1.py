class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dic={}
        def dp(i,holding):
            # 只考虑prices[i:]
            # holding指现在有没有股票
            if (i,holding) in dic: return dic[(i,holding)]
            if i>=n: return 0
            res=dp(i+1,holding) # do nothing
            if holding:
                res=max(res,prices[i]+dp(i+2,False)) # This is cooldown
            else:
                res=max(res,-prices[i]+dp(i+1,True))
            dic[(i,holding)]=res
            return res
        return dp(0,False)