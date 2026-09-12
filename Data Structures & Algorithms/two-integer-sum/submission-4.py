class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited={} # number to id
        for i,n in enumerate(nums):
            if target-n in visited:
                return [visited[target-n],i]
            else:
                visited[n]=i