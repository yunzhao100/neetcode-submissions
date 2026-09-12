class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        res=0
        # odd length
        for i in range(n):
            res+=1
            left,right=i-1,i+1
            while left>=0 and right<=n-1 and s[left]==s[right]:
                res+=1
                left-=1
                right+=1
        # even length
        for i in range(n):
            if i>=n-1: continue
            if s[i]!=s[i+1]:continue
            res+=1
            left,right=i-1,i+2
            while left>=0 and right<=n-1 and s[left]==s[right]:
                res+=1
                left-=1
                right+=1
        return res