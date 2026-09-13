class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dic={}
        m,n=len(text1),len(text2)
        def dp(i,j):
            if (i,j) in dic: return dic[(i,j)]
            if i>=m or j>=n: return 0
            res=0
            if text1[i]==text2[j]: res=1+dp(i+1,j+1)
            else: res=max(dp(i,j+1),dp(i+1,j))
            dic[(i,j)]=res
            return res
        return dp(0,0)