class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,n=0,len(s)
        st=set()
        res=0
        for r,c in enumerate(s):
            while c in st:
                st.remove(s[l])
                l+=1
            res=max(res,r-l+1)
            st.add(c)
        return res