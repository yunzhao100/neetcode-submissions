class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=defaultdict(int)
        for n in nums:
            freq[n]+=1
        lis=[[] for _ in range(len(nums)+1)]
        for n,freq in freq.items():
            lis[freq].append(n)
        res=[]
        for _ in lis[::-1]:
            for n in _:
                res.append(n)
            if len(res)==k:
                return res