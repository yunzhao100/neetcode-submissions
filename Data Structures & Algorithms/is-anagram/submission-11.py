class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1,dic2=defaultdict(int),defaultdict(int)
        for i in s:
            dic1[i]+=1
        for i in t:
            dic2[i]+=1
        return dic1==dic2