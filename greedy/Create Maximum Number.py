from typing import List


class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def maxinlist(self,nums,n):
            stack= []
            to_pop = len(nums) - n
            for num in nums:
                while to_pop !=0 and stack and  num > stack[-1]:
                    stack.pop()
                    to_pop -= 1
                stack.append(num)

            return stack[:n]
        


#     def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
#         num_list = list(set(nums1+nums2))
#         # print(num_list)
#
#     def fn(arrr, k):
#         """Return largest sub-sequence of arr of size k."""
#         ans = []
#         for i, x in enumerate(arrr):
#             while ans and ans[-1] < x and len(ans) + len(arrr) - i > k: ans.pop()
#             if len(ans) < k: ans.append(x)
#         return ans
#
#
# a=Solution()
# nums1 = [3,4,6,5]
# nums2 = [9,1,2,5,8,3]
# k = 5
#
# def fn(arr, k):
#     """Return largest sub-sequence of arr of size k."""
#     ans = []
#     for i, x in enumerate(arr):
#         while ans and ans[-1] < x and len(ans) + len(arr) - i > k:
#             ans.pop()
#         if len(ans) < k:
#             ans.append(x)
#     return ans

#

# # Example usage:




