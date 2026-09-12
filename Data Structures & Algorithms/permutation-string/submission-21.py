class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l,n=0,len(s2)
        counts1=defaultdict(int)
        countwindow=defaultdict(int)
        for i in s1:
            counts1[i]+=1
        for r in range(n):
            c=s2[r]
            countwindow[c]+=1
            while countwindow[c]>counts1[c]:
                countwindow[s2[l]]-=1
                l+=1
            if countwindow==counts1:
                return True
        return False