class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dic={}
        def dp(i):
            if i in dic: return dic[i]
            if i<n and int(s[i])==0: return 0
            if i==n: return 1
            if i>n: return 0
            if i==n-1: return 1 if s[-1]!=0 else 0
            res=0
            res+=dp(i+1)
            if int(s[i:i+2])<=26: res+=dp(i+2)
            dic[i]=res
            return dic[i]
        return dp(0)