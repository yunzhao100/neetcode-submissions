class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanumeric(i):
            return (ord('a')<=ord(i) and ord(i)<=ord('z')) or (ord('A')<=ord(i) and ord(i)<=ord('Z')) or (ord('0')<=ord(i) and ord(i)<=ord('9'))
        l,r=0,len(s)-1
        while l<r:
            if not alphanumeric(s[l]):
                l+=1
                continue
            if not alphanumeric(s[r]):
                r-=1
                continue
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
                continue
            else:
                return False
        return True