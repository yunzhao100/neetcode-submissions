class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dic={}
        def dp(i):
            if i>=n: return True
            if i in dic: return dic[i]
            res=False
            for word in wordDict:
                m=len(word)
                if i+m>n: continue
                if s[i:i+m]==word:
                    res=res or dp(i+m)
            dic[i]=res
            return res
        return dp(0)