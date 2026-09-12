class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            length=len(s)
            res+=str(length)+'#'+s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<=len(s)-1:
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+length+1
            res.append(s[j+1:i])
        return res