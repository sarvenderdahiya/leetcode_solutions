from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        map1 = {}
        intersec = []
        for i in nums1:
            if i in map1:
                map1[i] += 1
            else:
                map1[i] = 1

        for i in nums2:
            if i in map1:
                if map1[i] > 0:
                    intersec.append(i)
                    map1[i] -= 1

        return intersec