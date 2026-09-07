class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        res=[]

        zeros=0
        for num in nums:
            if num == 0:
                zeros+=1

        if zeros == 0:

            total=1
            for num in nums:
                total*=num
            
            for i in range(len(nums)):
                res.append(total // nums[i])
            return res
        
        elif zeros == 1:
            total = 1
            for num in nums:
                if num != 0:
                    total*=num
            
            for i in range(len(nums)):
                if nums[i] != 0:
                    res.append(0)
                else:
                    res.append(total)
            return res
        
        else:

            for i in range(len(nums)):
                res.append(0)
            return res
