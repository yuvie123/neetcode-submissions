class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        longest=0
        counter=0
        for i in range(len(nums)):

            #Check if it is a starting element:
            if nums[i] - 1 not in num_set:
                counter=0
                while (nums[i]+counter) in num_set:
                    counter+=1
                    longest = max(longest, counter)

        
        return longest