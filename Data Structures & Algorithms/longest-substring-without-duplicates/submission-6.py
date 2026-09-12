class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st=set()
        l,n=0,len(s)
        res=0
        for r in range(n):
            c=s[r]
            while c in st:
                st.remove(s[l])
                l+=1
            st.add(c)
            res=max(res,r-l+1)
        return res