class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==0:
            return 0
        min_=min(coins)
        dic={}
        for n in coins:
            dic[n]=1
        def dp(i):
            if i in dic:
                return dic[i]
            if i<min_:
                return -1
            dic[i]=float('inf')
            for n in coins:
                if dp(i-n)>=0:
                    dic[i]=min(dic[i],1+dp(i-n))
            if dic[i]==float('inf'):
                dic[i]=-1
            return dic[i]
        return dp(amount)