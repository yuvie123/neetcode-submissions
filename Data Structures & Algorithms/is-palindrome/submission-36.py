class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        L=0
        R=len(s)-1

        while L < R:
            
            if s[L].isalnum() != True:
                L+=1
            elif s[R].isalnum() != True:
                R-=1
            elif s[L].lower() == s[R].lower():
                L+=1
                R-=1
            else:
                return False
        return True