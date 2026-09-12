class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))+'#'+s
        return res
    def decode(self, s: str) -> List[str]:
        res=[]
        n=len(s)
        i=0
        while i < n:
            j=i
            while s[i]!='#':
                i+=1
            length=int(s[j:i])
            res.append(s[i+1:i+length+1])
            i=i+length+1
        return res