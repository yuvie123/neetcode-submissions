class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        chars = []
        for char in s:
            if char.isalnum():
                chars.append(char.lower())

        chars2 = chars.copy()
        chars2.reverse()

        return (chars == chars2)