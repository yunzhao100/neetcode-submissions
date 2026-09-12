class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
        # E: "4#neet4#code"

    def decode(self, s: str) -> List[str]:
        n = len(s)
        i = 0
        res = []
        while i<n:
            j=i
            while s[j]!="#":
                j+=1 # in case there are more than one digit
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j
        return res