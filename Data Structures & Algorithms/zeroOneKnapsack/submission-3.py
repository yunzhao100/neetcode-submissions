class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit)
        dic={}
        def dp(i,j):
            # most return from profit[:i] with capacity j
            if (i,j) in dic: return dic[(i,j)]
            if i<=0 or j<=0: return 0
            dic[(i,j)]=dp(i-1,j)
            remaining_capacity=j-weight[i-1]
            if remaining_capacity>=0:
                dic[(i,j)]=max(profit[i-1]+dp(i-1,remaining_capacity), dp(i-1,j))
            return dic[(i,j)]
        return dp(n,capacity)