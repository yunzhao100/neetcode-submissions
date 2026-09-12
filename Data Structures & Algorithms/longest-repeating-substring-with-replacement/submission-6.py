class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n=0,len(s)
        count=defaultdict(int)
        res=0
        mostF=0
        for r in range(n):
            count[s[r]]+=1
            mostF=max(mostF,count[s[r]])
            while l<r and r-l+1-mostF>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res