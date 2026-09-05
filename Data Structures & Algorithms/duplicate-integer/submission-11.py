class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        compare = []

        for num in nums:
            if num not in compare:
                compare.append(num)
            else:
                return True

        return False
