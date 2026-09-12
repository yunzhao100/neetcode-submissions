class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        res=''
        # odd length
        for i,c in enumerate(s):
            potential=c
            potential_len=1
            left=i-1
            right=i+1
            while left>=0 and right<=n-1 and s[left]==s[right]:
                if right-left+1>potential_len:
                    potential=s[left:right+1]
                    potential_len=right-left+1
                left-=1
                right+=1
            if potential_len>len(res):
                res=potential
        # even length
        for i,c in enumerate(s):
            if i>=n-1: continue
            if s[i]!=s[i+1]: continue
            potential=s[i:i+2]
            potential_len=2
            left=i-1
            right=i+2
            while left>=0 and right<=n-1 and s[left]==s[right]:
                if right-left+1>potential_len:
                    potential=s[left:right+1]
                    potential_len=right-left+1
                left-=1
                right+=1
            if potential_len>len(res):
                res=potential
        return res