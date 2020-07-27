from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return nums[i]

# Runtime: 60 ms, faster than 97.55% of Python3 online submissions
# Memory Usage: 16.1 MB, less than 97.34% of Python3 online submissions
