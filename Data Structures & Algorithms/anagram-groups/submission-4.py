class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for _ in s:
                freq[ord(_)-ord('a')]+=1
            res[tuple(freq)].append(s)
        return list(res.values())