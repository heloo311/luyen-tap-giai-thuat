from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        current_step = jumps = 0
        last_index= len(nums) -1
        while current_step < last_index:
            num = nums[current_step]
            start = current_step + 1
            end= start + num
            if end >= len(nums):
                jumps+=1
                break
            next_values = [nums[next_index] + next_index for next_index in list(range(start, end))]
            current_step += next_values.index(max(next_values)) + 1
            jumps += 1
        return jumps