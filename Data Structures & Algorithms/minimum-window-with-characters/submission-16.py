class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic=defaultdict(int)
        for i in t:
            dic[i]+=1
        m=len(dic)
        l,n=0,len(s)
        window=defaultdict(int)
        matched=0
        res=''
        resLen=n+1
        for r in range(n):
            c=s[r]
            window[c]+=1
            if dic[c]>0 and window[c]==dic[c]:
                matched+=1
            if matched==m:
                while window[s[l]]>dic[s[l]]:
                    window[s[l]]-=1
                    l+=1
                if resLen>r-l+1:
                    res=s[l:r+1]
                    resLen=len(res)
        return res