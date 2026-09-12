class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int) # n to count
        for n in nums:
            count[n]+=1
        group=[[] for _ in range(len(nums)+1)]
        for n in count:
            group[count[n]].append(n)
        res=[]
        length=0
        while len(res)<k:
            for n in group[-(length+1)]:
                res.append(n)
            length+=1
        return res