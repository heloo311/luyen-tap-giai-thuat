from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:

        l=0
        r=len(height) -1

        max_are=0

        while l < r:
            width = r-l
            length = min(height[l], height[r])

            max_are= max(max_are , width*length)

            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return max_are
height = [1,8,6,2,5,4,8,3,7]

a = Solution()

print(a.maxArea(height))




