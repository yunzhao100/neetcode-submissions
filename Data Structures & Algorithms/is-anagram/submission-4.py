class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        F1=defaultdict(int)
        F2=defaultdict(int)
        for i in s:
            F1[i]+=1
        for i in t:
            F2[i]+=1
        return F1==F2