class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        temp = set(nums)
        uniques = list(temp)
        uniques.sort()


        counter = 1
        greatest = 1
        for i in range(len(uniques)-1):

            if uniques[i + 1] - uniques[i] == 1:
                counter += 1
                greatest = max(counter, greatest)
            else:
                counter=1

        return greatest

 