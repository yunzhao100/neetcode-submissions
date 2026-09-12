class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dic={}
        def dp(i):
            # number of decoding ways in s[i:]
            if i>=n: return 1
            if i in dic: return dic[i]
            if s[i]=='0':
                return 0
            res=dp(i+1)
            if i+1<=n-1:
                if s[i]=='1' or (s[i]=='2' and int(s[i+1])<=6):
                    res+=dp(i+2)
            dic[i]=res
            return dic[i]
        return dp(0)