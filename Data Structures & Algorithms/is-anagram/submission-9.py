class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_freq,t_freq=defaultdict(int),defaultdict(int)
        for _ in s:
            s_freq[_]+=1
        for _ in t:
            t_freq[_]+=1
        return s_freq==t_freq