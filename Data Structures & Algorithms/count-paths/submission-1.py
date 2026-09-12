class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dic={}
        def dp(i,j):
            if (i,j) in dic: return dic[(i,j)]
            if i==m-1 or j==n-1: return 1
            res=dp(i+1,j)+dp(i,j+1)
            dic[(i,j)]=res
            return res
        return dp(0,0)