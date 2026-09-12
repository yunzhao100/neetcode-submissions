class Solution:
    def climbStairs(self, n: int) -> int:
        dic={1:1, 2:2}
        def dp(i):
            if i in dic:
                return dic[i]
            dic[i]=dp(i-1)+dp(i-2)
            return dic[i]
        return dp(n)