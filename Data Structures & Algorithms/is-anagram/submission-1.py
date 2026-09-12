class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = defaultdict(int)
        freq2 = defaultdict(int)
        for _ in s:
            freq1[_] += 1
        for _ in t:
            freq2[_] += 1
        return freq1 == freq2