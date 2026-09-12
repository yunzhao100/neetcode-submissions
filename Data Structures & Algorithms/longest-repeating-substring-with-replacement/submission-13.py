class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l,n=0,len(s)
        res=0
        max_freq=0
        dic=defaultdict(int)
        for r,c in enumerate(s):
            dic[c]+=1
            max_freq=max(max_freq,dic[c])
            while r-l+1-max_freq>k:
                dic[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res