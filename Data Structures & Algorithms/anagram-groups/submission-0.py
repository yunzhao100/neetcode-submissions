class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list) # ord to group
        for s in strs:
            count = [0] * 26
            for i in s:
                count[ord(i) - ord('a')] += 1
            dic[tuple(count)].append(s)
        return list(dic.values())