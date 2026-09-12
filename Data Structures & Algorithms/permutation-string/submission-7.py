class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,n=0,len(s2)
        count=defaultdict(int)
        for i in s1:
            count[i]+=1
        window=defaultdict(int)
        for r in range(n):
            c=s2[r]
            window[c]+=1
            while l<r and window[s2[l]]>count[s2[l]]:
                window[s2[l]]-=1
                l+=1
            if count==window:
                return True
        return False