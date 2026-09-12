class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res,buy=0,float('inf')
        for p in prices:
            if p<buy:
                buy=p
            res=max(res,p-buy)
        return res