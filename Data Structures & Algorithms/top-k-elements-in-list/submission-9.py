class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic=defaultdict(int) # n to freq
        for n in nums:
            dic[n]+=1
        lis=[[] for _ in range(len(nums)+1)]
        for n,freq in dic.items():
            lis[freq].append(n)
        res=[]
        for _ in lis[::-1]:
            for n in _:
                res.append(n)
            if len(res)==k:
                return res