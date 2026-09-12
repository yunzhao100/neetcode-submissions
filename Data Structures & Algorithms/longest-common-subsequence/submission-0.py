class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m,n=len(text1),len(text2)
        dic={}
        def dp(i,j):
            if (i,j) in dic: return dic[(i,j)]
            if i>m-1 or j>n-1: return 0
            dic[(i,j)]=max(dp(i+1,j),dp(i,j+1))
            if text1[i]==text2[j]:
                dic[(i,j)]=max(dic[(i,j)],1+dp(i+1,j+1))
            return dic[(i,j)]
        return dp(0,0)