class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        freq=[[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n]+=1
        for n,cnt in count.items():
            freq[cnt].append(n)
        res=[]
        for _ in range(len(freq)-1,-1,-1):
            for i in freq[_]:
                res.append(i)
            if len(res)==k:
                return res