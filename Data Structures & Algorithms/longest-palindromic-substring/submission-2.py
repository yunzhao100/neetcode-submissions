class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0: return ''
        res_id=(0,0)
        res_len=1
        for i in range(n):
            # odd length
            l,r=i,i
            while l>=0 and r<=n-1 and s[l]==s[r]:
                if r-l+1>res_len:
                    res_id=(l,r)
                    res_len=r-l+1
                l-=1
                r+=1
            # even length
            l,r=i,i+1
            while l>=0 and r<=n-1 and s[l]==s[r]:
                if r-l+1>res_len:
                    res_id=(l,r)
                    res_len=r-l+1
                l-=1
                r+=1
        l,r=res_id
        return s[l:r+1]