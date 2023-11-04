from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # first_digits = [int(str(num)[0]) for num in nums]
        # print(first_digits)
        #
        #
        #
        # sorted_indices = sorted(range(len(first_digits)), key=lambda i: first_digits[i], reverse=True)
        # print(sorted_indices)
        #
        # sorted_nums = [nums[i] for i in sorted_indices]
        #
        # print(sorted_nums)
        #
        # one_digit_nums = [num for num in sorted_nums if num < 10]
        # multi_digit_nums = [num for num in sorted_nums if num >= 10]
        # sorted_multi_digit_nums = sorted(multi_digit_nums,reverse=True)
        # sorted_nums = one_digit_nums + sorted_multi_digit_nums
        #
        # print(sorted_nums)
        if len(nums) == 1:
            return str(nums[0])

        count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                count += 1
            nums[i] = str(nums[i])

        if count == len(nums):
            return '0'

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if int(nums[j] + nums[i]) > int(nums[i] + nums[j]):
                    nums[i], nums[j] = nums[j], nums[i]

        return ''.join(nums)

a= Solution()
nums = [3,30,34,5,9]
print(a.largestNumber(nums))
nums = [9, 5, 3, 30, 34]









