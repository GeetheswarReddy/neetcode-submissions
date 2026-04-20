class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=''
        s=s.lower()
        for i in range(len(s)):
            if s[i].isalnum():
                y=y+s[i]
        l=len(y)-1
        i=0
        while(i<=l):
            if y[i]!=y[l]:
                return False
            i+=1
            l-=1
        return True
            
        