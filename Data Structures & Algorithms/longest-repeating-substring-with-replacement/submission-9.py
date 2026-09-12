class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n=0,len(s)
        res=0
        window=defaultdict(int)
        mostF=0
        for r in range(n):
            c=s[r]
            window[c]+=1
            mostF=max(mostF,window[c])
            while r-l+1-mostF>k:
                window[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res