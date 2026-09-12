class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic={0:0}
        def dp(i):
            if i<0:
                return -1
            if i in dic:
                return dic[i]
            best=float('inf')
            for n in coins:
                time=dp(i-n)
                if time!=-1:
                    best=min(best,1+time)
            dic[i]=best if best!=float('inf') else -1
            return dic[i]
        return dp(amount)