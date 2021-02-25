from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False
        hset = set()
        for num in nums:
            if num in hset:
                return True
            hset.add(num)
        return False