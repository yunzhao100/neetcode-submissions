class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n=0,len(s)
        res=0
        dic=defaultdict(int)
        alpha,freq=s[l],1
        for r in range(n):
            c=s[r]
            dic[c]+=1
            if dic[c]>freq:
                alpha,freq=c,dic[c]
            while freq+k<r-l+1:
                dic[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res