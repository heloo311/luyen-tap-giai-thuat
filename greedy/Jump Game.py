from typing import List


# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         i=0
#         n= len(nums)-1
#         while i< n:
#
#
#             temp = nums[i]
#
#             i+= temp
#
#             if i >= n:
#                 return True
#
#             return False
#
# a= Solution()
#
# nums = [2,3,1,1,4]
#
# print(a.canJump(nums))

# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         i = 0
#         n= len(nums)-1
#
#         longest = 0
#
#         while i < n:
#             temp = nums[i]
#
#             longest = max(temp , longest)
# nums = [2,3,1,1,4]
# for index in range(len(nums)-1,-1,-1):
#     print(index)


