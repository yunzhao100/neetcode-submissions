class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count=defaultdict(int)
        for _ in s1:
            count[_]+=1
        l,n=0,len(s2)
        count2=defaultdict(int)
        for r in range(n):
            count2[s2[r]]+=1
            while l<r and count2[s2[l]]>count[s2[l]]:
                count2[s2[l]]-=1
                l+=1
            if count2==count:
                return True
        return False