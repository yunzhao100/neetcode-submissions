class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphanumeric(s):
            return (ord('a')<=ord(s) and ord(s)<=ord('z')) or (ord('A')<=ord(s) and ord(s)<=ord('Z')) or (ord('0')<=ord(s) and ord('9')>=ord(s))
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