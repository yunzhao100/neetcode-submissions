class Solution:
    def climbStairs(self, n: int) -> int:
        dic={}
        def dp(i):
            if i<=2: return i
            if i in dic: return dic[i]
            res=dp(i-1)+dp(i-2)
            dic[i]=res
            return res
        return dp(n)