class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy,n=float('inf'),len(prices)
        res=0
        for sell in prices:
            if sell<buy:
                buy=sell
            res=max(res,sell-buy)
        return res