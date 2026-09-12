class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dic={}
        def dp(i,j):
            # total paths from (i,j) to (m-1,n-1)
            if (i,j) in dic: return dic[(i,j)]
            if i==m-1 or j==n-1: return 1
            dic[(i,j)]=dp(i+1,j)+dp(i,j+1)
            return dic[(i,j)]
        return dp(0,0)