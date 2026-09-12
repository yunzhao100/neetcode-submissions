class Solution:
    def climbStairs(self, n: int) -> int:
        dic={1:1, 2:2}
        def dp(n):
            if n in dic:
                return dic[n]
            dic[n]=dp(n-1)+dp(n-2)
            return dic[n]
        return dp(n)