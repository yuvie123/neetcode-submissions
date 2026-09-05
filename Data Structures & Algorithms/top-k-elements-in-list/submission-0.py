class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        for item in nums:

            if item in hashmap:
                hashmap[item] = hashmap[item] + 1
            else:
                hashmap[item] = 1
        
        freqs = []
        for key in hashmap:
            freqs.append(hashmap[key])
        
        freqs.sort(reverse=True)
        freqs = freqs[0:k]
        mostFreq=[]

        for key in hashmap:
            if hashmap[key] in freqs:
                mostFreq.append(key)
        
        return mostFreq
        
            


        
        
