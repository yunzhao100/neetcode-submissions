class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n=0,len(s)
        res=0
        mostF=0
        count=defaultdict(int)
        for r in range(n):
            c=s[r]
            count[c]+=1
            mostF=max(mostF,count[c])
            while r-l+1-mostF>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res