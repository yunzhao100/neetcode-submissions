class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        while l<r:
            while l<r and not self.AlphaNum(s[l]):
                l+=1
            while l<r and not self.AlphaNum(s[r]):
                r-=1
            if s[l].lower()==s[r].lower():
                l+=1
                r-=1
            else:
                return False
        return True
    def AlphaNum(self,s):
        return (ord(s)>=ord('a') and ord(s)<=ord('z')) or (ord(s)>=ord('A') and ord(s)<=ord('Z')) or (ord(s)>=ord('0') and ord(s)<=ord('9'))