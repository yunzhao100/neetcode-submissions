class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic=defaultdict(list)
        for s in strs:
            freq=[0]*26
            for i in s:
                freq[ord(i)-ord('a')]+=1
            dic[tuple(freq)].append(s)
        return list(dic.values())