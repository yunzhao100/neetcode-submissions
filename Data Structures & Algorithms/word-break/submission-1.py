class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dic={}
        def dp(i):
            if i>=n: return True
            if i in dic: return dic[i]
            res=False
            for word in wordDict:
                if i+len(word)<=n and s[i:i+len(word)]==word:
                    res=res or dp(i+len(word))
            dic[i]=res
            return res
        return dp(0)