class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n=0,len(s)
        res=0
        count={}
        for r in range(n):
            count[s[r]] = 1+count.get(s[r],0)
            while r-l+1-max(count.values())>k:
                count[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res