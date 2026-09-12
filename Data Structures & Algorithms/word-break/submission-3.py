class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dic={}
        def dp(i):
            if i>=n: return True
            if i in dic: return dic[i]
            res=False
            for w in wordDict:
                if i+len(w)<=n and s[i:i+len(w)]==w:
                    res=res or dp(i+len(w))
            dic[i]=res
            return res
        return dp(0)