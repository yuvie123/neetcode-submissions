class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Same start if they aren't the same len then do

        if len(s) != len(t):
            return False

        count = [0] * 26   # This creates an array with 25 indexes

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        for freq in count:
            if freq != 0:
                return False
        return True

        