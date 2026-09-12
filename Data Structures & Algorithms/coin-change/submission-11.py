class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic={}
        def dp(i):
            if i==0: return 0
            if i<0: return -1
            if i in dic: return dic[i]
            res=float('inf')
            for c in coins:
                if dp(i-c)!=-1:
                    res=min(res,1+dp(i-c))
            res=-1 if res==float('inf') else res
            dic[i]=res
            return res
        return dp(amount)