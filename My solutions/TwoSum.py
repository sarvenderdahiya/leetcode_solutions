# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List

# ************ OLD OUTDATED SLOW NAIVE SOLUTION **********************
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         x = 0
#         for i in nums:
#             y = 0
#             for j in nums:
#                 if target == (i + j) and x != y:
#                     return x, y
#                 y = y + 1
#             x = x + 1


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {nums[0]: 0}

        for k, v in enumerate(nums[1:], start=1):
            if target - v in hashmap:
                return [k, hashmap[target - v]]

            hashmap[v] = k
