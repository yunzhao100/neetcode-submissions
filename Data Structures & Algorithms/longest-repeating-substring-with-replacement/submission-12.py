class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        maxF=0
        l,n=0,len(s)
        res=0
        for r in range(n):
            c=s[r]
            count[c]+=1
            maxF=max(maxF,count[c])
            while r-l+1-maxF>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res