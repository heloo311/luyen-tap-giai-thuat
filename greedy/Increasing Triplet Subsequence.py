import math
from typing import List


class Solution:
    # def increasingTriplet(self, nums: List[int]) -> bool:
#     #     stack= []
#     #     dem = []
#     #     for i in range(len(nums) ):
#     #         while stack and nums[i] < stack[-1]:
#     #             stack.pop()
#     #         stack.append(nums[i])
#     #
#     #         if len(stack) >=3:
#     #             print(stack)
#     #             return True
#     #
#     #
#     #     return False

    def increasingTriplet(self, nums: List[int]) -> bool:
        arr = [math.inf] * 3
        for num in nums:
            if num <= arr[0]:
                arr[0] = num
            elif num <= arr[1]:
                arr[1] = num
            else:
                return True
        return False
a= Solution()
nums = [2,1,5,0,4,6]
print(a.increasingTriplet(nums))

for i in range(len(nums)):
    print(nums[i])