from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        idxsum = 99999
        result = []
        map1 = {}
        for i in range(len(list1)):
            map1[list1[i]] = i

        for i in range(len(list2)):
            if list2[i] in map1:
                if i + map1[list2[i]] < idxsum:
                    idxsum = i + map1[list2[i]]
                    result.clear()
                    result.append(list2[i])
                elif i + map1[list2[i]] == idxsum:
                    result.append(list2[i])

        return result

o = Solution()

print(o.findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"], ["KFC","Burger King","Tapioca Express","Shogun"]))