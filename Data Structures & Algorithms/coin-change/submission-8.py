class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0: return 0
        dic={}
        def dp(i):
            if i in coins: return 1
            if i<0: return -1
            if i==0: return 0
            if i in dic: return dic[i]
            dic[i]=float('inf')
            for n in coins:
                if dp(i-n)>=0:
                    dic[i]=min(dic[i],1+dp(i-n))
            if dic[i]==float('inf'): dic[i]=-1
            return dic[i]
        return dp(amount)