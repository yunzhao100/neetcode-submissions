class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for _ in s:
                freq[ord(_)-ord('a')]+=1
            dic[tuple(freq)].append(s)
        return list(dic.values())