class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        L = 0
        R = len(numbers) - 1

        while L < R:
            summation = numbers[L] + numbers[R]

            if summation == target:
                return [L+1, R+1]
            elif summation > target:
                R-=1
            elif summation < target:
                L+=1
            
