class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        hashmap = {}
        
        for num in nums: # This is O(n)

            if num in hashmap: # This is O(1) -> is it a hashmap look up
            # So it keeps time complexity at O(n)
                return True

            hashmap[num] = 0
        
        return False



