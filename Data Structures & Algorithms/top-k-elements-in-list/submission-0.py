class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # creat a count (dict); 
        # bucket sort count in freq (list of lists)
        # backward loop freq, add the numbers to res
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n] += 1
        for n, cnt in count.items():
            freq[cnt].append(n)
        
        res = []
        for _ in range(len(freq)-1, -1, -1):
            for n in freq[_]:
                res.append(n)
            if len(res) == k:
                return res