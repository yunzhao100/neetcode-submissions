class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        res=0
        for sell in prices:
            if sell>buy:
                res=max(res,sell-buy)
            else:
                buy=sell
        return res