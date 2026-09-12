class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dic={}
        def dp(i,j):
            if i>=m or j>=n: return 0
            if (i,j) in dic: return dic[(i,j)]
            res=max(dp(i,j+1),dp(i+1,j))
            if text1[i]==text2[j]:
                res=max(res,1+dp(i+1,j+1))
            dic[(i,j)]=res
            return res
        return dp(0,0)