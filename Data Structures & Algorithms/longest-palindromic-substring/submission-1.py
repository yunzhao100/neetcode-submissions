class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        if n==0: return ''
        res_left,res_right=0,0
        # odd length
        for i in range(n):
            curr_left,curr_right=i,i
            curr_len=1
            left=i-1
            right=i+1
            while left>=0 and right<=n-1 and s[left]==s[right]:
                if right-left+1>curr_len:
                    curr_left=left
                    curr_right=right
                    curr_len=right-left+1
                left-=1
                right+=1
            if curr_len>res_right-res_left+1:
                res_left,res_right=curr_left,curr_right
        # even length
        for i,c in enumerate(s):
            if i>=n-1: continue
            if s[i]!=s[i+1]: continue
            curr_left,curr_right=i,i+1
            curr_len=2
            left=i-1
            right=i+2
            while left>=0 and right<=n-1 and s[left]==s[right]:
                if right-left+1>curr_len:
                    curr_left=left
                    curr_right=right
                    curr_len=right-left+1
                left-=1
                right+=1
            if curr_len>res_right-res_left+1:
                res_left,res_right=curr_left,curr_right
        return s[res_left:res_right+1]