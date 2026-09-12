class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        L = 0
        R = len(heights) - 1

        area = 0;
        greatest = 0

        while L < R:

            area = (R - L) * (min(heights[L], heights[R]))
            greatest = max(area, greatest)

            if heights[L] > heights[R]:
                R-=1
            elif heights[L] < heights[R]:
                L+=1
            else:
                L+=1
                R-=1
    
            

        return greatest
