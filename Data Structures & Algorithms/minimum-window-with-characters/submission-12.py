class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT=defaultdict(int)
        for i in t:
            countT[i]+=1
        l,n=0,len(s)
        countwindow=defaultdict(int)
        have=0
        need=len(countT)
        res=[-1,-1]
        for r in range(n):
            c=s[r]
            countwindow[c]+=1
            if countwindow[c]==countT[c]:
                have+=1
            while have==need:
                res=[l,r]
                countwindow[s[l]]-=1
                if countwindow[s[l]]<countT[s[l]]:
                    have-=1
                l+=1
        L,R=res
        if res==[-1,-1]:
            return ''
        else:
            return s[L:R+1]