class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums=list(range(1,n+1))
        path=[]
        res=[]
        def dfs(i):
            if len(path)==k:
                res.append(path.copy())
                return
            if n-i<k-len(path):
                return
            for j in range(i,n):
                path.append(nums[j])
                dfs(j+1)
                path.pop()
            return
        dfs(0)
        return res