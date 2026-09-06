class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        # NOTE THAT YOU CAN NOT MODIFY A KEY IN PYTHON SO LISTS DON'T WORK AS KEYS
        # WE CAN USE A TUPLE INSTEAD

        # NOTE THAT APPEND DOES NOT RETURN ANYTHING 
        
        hashmap = {}
        anagrams = []

        for word in strs:
            count = [0] * 26
            
            for char in word:
                count[ord(char) - ord('a')] += 1

            count = tuple(count)
            if count in hashmap:
                hashmap[count].append(word)
            else:
                hashmap[count] = [word]
    
        for key in hashmap:
            anagrams.append(hashmap[key])
        
        return anagrams





        
        

        
        