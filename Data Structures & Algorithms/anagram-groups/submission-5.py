class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for i in s:
                freq[ord(i)-ord('a')]+=1
            res[tuple(freq)].append(s)
        return res.values()