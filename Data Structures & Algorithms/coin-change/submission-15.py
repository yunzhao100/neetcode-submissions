class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic={}
        # dp(i): number of coins needed when the amount is i
        def dp(i):
            if i in dic: return dic[i]
            if i in coins: return 1
            if i==0: return 0
            if i<0: return -1 # -1 means impossible
            # for each coin, compare which one should use in the combination
            res=float('inf')
            for c in coins:
                remaining=dp(i-c)
                if remaining>0:
                    res=min(res,remaining+1)
            dic[i]=res if res<float('inf') else -1
            return dic[i]
        return dp(amount)