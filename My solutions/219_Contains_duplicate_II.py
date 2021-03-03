from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        map1 = {}
        for i, num in enumerate(nums):
            if num in map1 and i - map1[num] <= k:
                return True
            map1[nums[i]] = i
        return False
