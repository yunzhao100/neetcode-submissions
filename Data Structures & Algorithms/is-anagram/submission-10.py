class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1,dic2=defaultdict(int),defaultdict(int)
        for _ in s:
            dic1[_]+=1
        for _ in t:
            dic2[_]+=1
        return dic1==dic2