from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        hset1 = set()
        hset2 = set()
        for i in nums1:
            hset1.add(i)

        for i in nums2:
            hset2.add(i)

        return list(hset1.intersection(hset2))