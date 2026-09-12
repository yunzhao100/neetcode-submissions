class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            length=len(s)
            res+=str(length)
            res+='#'
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<=len(s)-1:
            k=i
            while s[k]!='#':
                k+=1
            length=int(s[i:k])
            string=s[k+1:k+length+1]
            res.append(string)
            i=k+length+1
        return res