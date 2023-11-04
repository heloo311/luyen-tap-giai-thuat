from itertools import accumulate


class Solution:
    def maxSubArray(self, nums):
        def helper(beg, end):
            if beg + 1 == end: return nums[beg]
            mid = (beg + end)//2
            sum_1 = helper(beg, mid)
            sum_2 = helper(mid, end)
            right = max(accumulate(nums[beg:mid][::-1]))
            left  = max(accumulate(nums[mid:end]))
            print(mid)
            # print(sum_2)
            return max(sum_1, sum_2, left + right)

        return helper(0, len(nums))

    def maxSubArray(self, nums):
        dp = [0] * len(nums)

        for i, num in enumerate(nums):
            dp[i] = max(dp[i - 1] + num, num)
        return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]

a=Solution()
print(a.maxSubArray(nums))

