class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        output = []
        
        for i, num in enumerate(nums):
            target = num * -1

            if i!=0 and num == nums[i-1]:
                continue

            else:
                L = i + 1
                R = len(nums) - 1

                while L < R:

                    summation = nums[L] + nums[R]
                    
                    if summation == target:
                        output.append([num, nums[L], nums[R]])
                        L+=1
                        while L < R and nums[L] == nums[L-1]:
                                L+=1
                    elif summation > target:
                        R-=1
                    elif summation < target:
                        L+=1

                
        return output

        