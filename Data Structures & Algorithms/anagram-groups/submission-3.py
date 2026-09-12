class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for _ in s:
                freq[ord(_)-ord('a')]+=1
            group[tuple(freq)].append(s)
        return list(group.values())