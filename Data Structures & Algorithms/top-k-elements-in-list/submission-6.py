class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqMap = {}
        freq=[]
        for i in range(len(nums) + 1):
            freq.append([])
        
        for num in nums:
            freqMap[num] = 1 + freqMap.get(num, 0)
        
        for key in freqMap:
            freq[freqMap[key]].append(key)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

