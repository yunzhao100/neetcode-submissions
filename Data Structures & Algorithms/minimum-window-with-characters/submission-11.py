class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count=defaultdict(int)
        for i in t:
            count[i]+=1
        l,n=0,len(s)
        have,need=0,len(count)
        res,resLen=[-1,-1],n+1
        window=defaultdict(int)
        for r in range(n):
            c=s[r]
            window[c]+=1
            if window[c]==count[c]:
                have+=1
            while have==need:
                if r-l+1<resLen:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if window[s[l]]<count[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen<n+1 else ''