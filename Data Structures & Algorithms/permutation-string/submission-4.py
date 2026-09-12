class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1=defaultdict(int)
        for s in s1:
            count1[s]+=1
        l=0
        count2=defaultdict(int)
        for r,s in enumerate(s2):
            count2[s]+=1
            while l<r and count2[s2[l]]>count1[s2[l]]:
                count2[s2[l]]-=1
                l+=1
            if count2==count1:
                return True
        return False