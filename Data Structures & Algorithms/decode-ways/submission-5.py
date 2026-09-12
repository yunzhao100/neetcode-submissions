class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dic={}
        def dp(i):
            if i>=n: return 1
            if s[i]=='0': return 0
            if i in dic: return dic[i]
            res=dp(i+1)
            if i+1<=n-1 and (s[i]=='1' or (s[i]=='2' and s[i+1] in '0123456')):
                res+=dp(i+2)
            dic[i]=res
            return res
        return dp(0)