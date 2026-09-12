class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,n=0,len(s)
        res=0
        st=set()
        for r in range(n):
            while s[r] in st:
                st.remove(s[l])
                l+=1
            st.add(s[r])
            res=max(res,len(st))
        return res