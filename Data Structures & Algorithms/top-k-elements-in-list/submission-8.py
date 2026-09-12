class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
        group=[[] for _ in range(len(nums)+1)]
        for n,cnt in count.items():
            group[cnt].append(n)
        res=[]
        for numbers in group[::-1]:
            for n in numbers:
                res.append(n)
            if len(res)==k:
                return res