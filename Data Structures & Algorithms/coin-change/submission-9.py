class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic={}
        def dp(i):
            if i in dic: return dic[i]
            if i in coins: return 1
            if i==0: return 0
            if i<0: return -1
            dic[i]=float('inf')
            for n in coins:
                if dp(i-n)>0:
                    dic[i]=min(dic[i],dp(i-n)+1)
            return dic[i] if dic[i]!=float('inf') else -1
        return dp(amount)