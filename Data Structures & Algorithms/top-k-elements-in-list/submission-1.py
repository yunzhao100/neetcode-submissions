class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        freq=[[] for _ in range(len(nums)+1)]
        for n in nums:
            count[n]+=1
        for n in count.keys():
            freq[count[n]].append(n)
        res=[]
        for i in range(len(freq)-1,-1,-1):
            for _ in freq[i]:
                res.append(_)
            if len(res)==k:
                break
        return res