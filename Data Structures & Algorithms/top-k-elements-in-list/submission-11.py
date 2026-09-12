class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        for n in nums:
            count[n]+=1
        freq=[[] for _ in range(len(nums)+1)]
        for n,cnt in count.items():
            freq[cnt].append(n)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for j in freq[i]:
                res.append(j)
            if len(res)==k:
                return res