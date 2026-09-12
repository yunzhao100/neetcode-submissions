class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dic={}
        def dp(i,hold):
            if (i,hold) in dic: return dic[(i,hold)]
            if i>=n: return 0
            res=dp(i+1,hold)
            if hold:
                res=max(res,prices[i]+dp(i+2,not hold))
            else:
                res=max(res,-prices[i]+dp(i+1,not hold))
            dic[(i,hold)]=res
            return res

        return dp(0,False)