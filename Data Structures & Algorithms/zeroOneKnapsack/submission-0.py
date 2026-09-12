class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit) # n个item
        dic={}
        def dp(i,j):
            # 前(i+1)个item可以拿
            # capacity是j
            # 返回最大利润
            if (i,j) in dic: return dic[(i,j)]
            if i<0 or j<0: return 0
            dic[(i,j)]=dp(i-1,j) # 不拿第(i+1)个item
            remain_capacity=j-weight[i]
            if remain_capacity>=0:
                dic[(i,j)]=max(dic[(i,j)],profit[i]+dp(i-1,remain_capacity))
                # 可能需要拿第(i+1)个
            return dic[(i,j)]
        return dp(n-1,capacity)