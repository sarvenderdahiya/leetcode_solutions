from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hset = set()
        for num in nums:
            if num in hset:
                hset.remove(num)
            else:
                hset.add(num)
        return hset.pop()


