class Solution:


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash_anagram = {}

        index=0
        for word in strs:

            word = "".join(sorted(word))
            if word not in hash_anagram:
                hash_anagram[word] = index
                index+=1

        anagrams=[]
        for i in range(index):
            anagrams.append([])
        
        temp=""
        for word in strs:
            temp = "".join(sorted(word))

            anagrams[hash_anagram[temp]].append(word)
        
        return anagrams


                    