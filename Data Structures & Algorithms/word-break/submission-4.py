class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dic={}
        n=len(s)
        def dp(i):
            if i in dic: return dic[i]
            if i>=n: return True
            sub=s[i:]
            if sub in wordDict: return True
            res=False
            for j in range(len(sub)):
                subsub=sub[:j+1]
                if subsub in wordDict and dp(i+j+1):
                    res=True
                    break
            dic[i]=res
            return dic[i]
        return dp(0)