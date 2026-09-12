class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
        group=[[] for _ in range(len(nums)+1)]
        for n,f in count.items():
            group[f].append(n)
        res=[]
        for i in range(len(group)-1,-1,-1):
            for n in group[i]:
                res.append(n)
            if len(res)==k:
                return res