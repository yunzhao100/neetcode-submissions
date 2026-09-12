class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n=len(profit)
        dic={} # (i,j): 前(i+1)个item，capacity是j
        for i in range(n):
            dic[(i,0)]=0
        for j in range(capacity+1):
            dic[(-1,j)]=0
        for i in range(n):
            for j in range(capacity+1):
                dic[(i,j)]=dic[(i-1,j)]
                if j-weight[i]>=0:
                    dic[(i,j)]=max(dic[(i,j)],profit[i]+dic[(i-1,j-weight[i])])
        return dic[(n-1,capacity)]