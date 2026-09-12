class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        for n in nums:
            count[n] = 1+count.get(n,0)
        group=[[] for _ in range(len(nums)+1)]
        for n,f in count.items():
            group[f].append(n)
        res=[]
        for i in range(len(group)-1,-1,-1):
            for _ in group[i]:
                res.append(_)
            if len(res)==k:
                return res