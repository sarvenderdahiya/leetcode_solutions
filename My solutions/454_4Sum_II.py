from typing import List
from collections import Counter
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        AB = [x+y for x in A for y in B]
        CD = [x+y for x in C for y in D]
        ans = 0
        ABcounter = Counter(AB)
        CDcounter = Counter(CD)

        for val in ABcounter:
            if -val in CDcounter:
                ans += ABcounter[val] * CDcounter[-val]

        return ans

# o = Solution()
# print(o.fourSumCount([0,1,-1],[-1,1,0],[0,0,1],[-1,1,1]))
# Should print 17