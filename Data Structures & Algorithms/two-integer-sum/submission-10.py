class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            n=nums[i]
            rem=target-n
            if rem in dic:
                return [dic[rem],i]
            dic[n]=i
        return -1