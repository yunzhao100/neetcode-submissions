class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic=defaultdict(int)
        for i in s1:
            dic[i]+=1
        l,n=0,len(s2)
        window=defaultdict(int)
        for r in range(n):
            c=s2[r]
            window[c]+=1
            while window[c]>dic[c]:
                window[s2[l]]-=1
                l+=1
            if window==dic:
                return True
        return False