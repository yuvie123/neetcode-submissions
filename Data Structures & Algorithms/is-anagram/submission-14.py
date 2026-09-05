class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        word1 = "".join(sorted(s))
        word2 = "".join(sorted(t))

        return word1 == word2
        