class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1, count2 = {}, {}
        for s_ in s:
            count1[s_] = count1.get(s_, 0) + 1
        for t_ in t:
            count2[t_] = count2.get(t_, 0) + 1
        return count1 == count2