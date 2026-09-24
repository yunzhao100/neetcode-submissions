class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        path=[]
        res=[]
        used=[False]*n
        def dfs():
            if len(path)==len(nums):
                res.append(path.copy())
                return
            for i in range(n):
                if used[i]: continue
                path.append(nums[i])
                used[i]=True
                dfs()
                used[i]=False
                path.pop()
            return
        dfs()
        return res