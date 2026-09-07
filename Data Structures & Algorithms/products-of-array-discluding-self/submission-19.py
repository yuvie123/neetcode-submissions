class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        zeros = 0
        for x in nums:
            if x == 0:
                zeros += 1


        if zeros > 1:
            res = []
            for x in nums:
                res.append(0)
            return res

        if zeros == 1:
            prod = 1
            for x in nums:
                if x != 0:
                    prod *= x

            res = []
            for x in nums:
                if x == 0:
                    res.append(prod)
                else:
                    res.append(0)
            return res

        total = 1
        for x in nums:
            total *= x

        res = []
        for x in nums:
            res.append(total // x)
        return res