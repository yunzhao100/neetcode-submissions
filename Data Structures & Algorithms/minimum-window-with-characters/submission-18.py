class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic1=defaultdict(int)
        for i in t:
            dic1[i]+=1
        m=len(dic1)
        l,n=0,len(s)
        dic2=defaultdict(int)
        filled=0
        res,resLen='',n+1
        for r in range(n):
            c=s[r]
            dic2[c]+=1
            if dic2[c]==dic1[c]:
                filled+=1
            while filled==m:
                if r-l+1<resLen:
                    res=s[l:r+1]
                    resLen=r-l+1
                dic2[s[l]]-=1
                if dic2[s[l]]<dic1[s[l]]:
                    filled-=1
                l+=1
            
        return res