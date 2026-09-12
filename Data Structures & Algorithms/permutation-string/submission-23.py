class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1=defaultdict(int)
        for i in s1:
            dic1[i]+=1
        l,n=0,len(s2)
        dic2=defaultdict(int)
        for r in range(n):
            c=s2[r]
            dic2[c]+=1
            if dic1==dic2:
                return True
            while dic2[c]>dic1[c]:
                dic2[s2[l]]-=1
                l+=1
        return False