class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        prefix = [1]
        postfix = [1]
        total = 1


        for i in range(len(nums)):
            total *= nums[i]
            prefix.append(total)

        total=1
        for i in range(len(nums)-1, -1, -1):
            total *= nums[i]
            postfix.append(total)

        postfix.reverse()

        res=[]
        for i in range(len(nums)):
            res.append(prefix[i])
            res[i] *= postfix[i+1]
        

        return res
