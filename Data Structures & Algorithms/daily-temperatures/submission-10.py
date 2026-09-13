class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # dp(i): in temperatures[i+1:], how many days to see a warmer day than temparatures[i]
        dic={}
        n=len(temperatures)
        def dp(i):
            if i in dic: return dic[i]
            if i>=n-1: return 0
            res=0
            k=i+1
            curr=temperatures[i]
            while k<n:
                if temperatures[k]>curr:
                    res=k-i
                    break
                add_=dp(k)
                if add_==0:
                    dic[i]=0
                    return dic[i]
                k=k+add_
            dic[i]=res
            return res
        for i in range(n-1,-1,-1): dp(i)
        return [dp(i) for i in range(n)]