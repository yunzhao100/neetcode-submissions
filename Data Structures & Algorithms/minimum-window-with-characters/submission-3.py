class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=='':
            return ''
        countT={}
        window={}
        for _ in t:
            countT[_]=1+countT.get(_,0)
        need, have = len(countT), 0
        l=0
        res, resLen=[-1,-1], float('inf')
        for r in range(len(s)):
            c=s[r]
            window[c]=1+window.get(c,0)
            if c in countT and window[c]==countT[c]:
                have+=1
            while have==need:
                if resLen>r-l+1:
                    res=[l,r]
                    resLen=r-l+1
                window[s[l]]-=1
                if s[l] in countT and window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float('inf') else ''