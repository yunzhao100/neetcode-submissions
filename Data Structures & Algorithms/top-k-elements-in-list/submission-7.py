class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
        freq=[[] for _ in range(len(nums)+1)]
        for n,cnt in count.items():
            freq[cnt].append(n)
        res=[]
        for numbers in freq[::-1]:
            for n in numbers:
                res.append(n)
            if len(res)==k:
                return res