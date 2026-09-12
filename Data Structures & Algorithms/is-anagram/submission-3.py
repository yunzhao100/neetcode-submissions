class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1={}
        count2={}
        for _ in s:
            count1[_] = 1+count1.get(_, 0)
        for _ in t:
            count2[_] = 1+count2.get(_, 0)
        return count1==count2