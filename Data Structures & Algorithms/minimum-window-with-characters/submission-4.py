class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=='':
            return ''
        countT=defaultdict(int)
        for _ in t:
            countT[_]+=1
        window=defaultdict(int)
        need,have=len(countT),0
        l=0
        res=[-1,-1]
        resLen=float('inf')
        for r in range(len(s)):
            c=s[r]
            window[c]+=1
            if window[c]==countT[c]:
                have+=1
            while have==need:
                if r-l+1<resLen:
                    resLen=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float('inf') else ''