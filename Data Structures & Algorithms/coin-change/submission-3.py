class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dic={}
        for n in coins:
            dic[n]=1
        def dp(i):
            if i==0:
                return 0
            if i<0:
                return -1
            if i in dic:
                return dic[i]
            next_=set()
            for n in coins:
                if n<i and dp(i-n)!=-1:
                    next_.add(dp(i-n))
            if len(next_)==0:
                dic[i]=-1
                return dic[i]
            dic[i]=1+min(next_)
            return dic[i]
        return dp(amount)