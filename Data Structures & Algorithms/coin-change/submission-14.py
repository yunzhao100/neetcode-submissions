class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Let dp(i) mean: The minimum number of coins needed to make exactly amount i.
        dic={}
        def dp(i):
            if i==0: return 0
            if i<0: return -1 # -1 means impossible
            if i in dic: return dic[i]
            res=float('inf')
            for c in coins:
                remaining=dp(i-c)
                if remaining!=-1:
                    res=min(res,1+remaining)
            res=-1 if res==float('inf') else res
            dic[i]=res
            return res
        return dp(amount)