class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s=='':
            return ''
        countT=defaultdict(int)
        for _ in t:
            countT[_]+=1
        l,n=0,len(s)
        have,need=0,len(countT)
        window=defaultdict(int)
        res,resLen=[-1,-1],float('inf')
        for r in range(n):
            c=s[r]
            window[c]+=1
            if window[c]==countT[c]:
                have+=1
            while have==need:
                if r-l+1<resLen:
                    res,resLen=[l,r],r-l+1
                window[s[l]]-=1
                if window[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        l,r=res
        return s[l:r+1] if resLen!=float('inf') else ''