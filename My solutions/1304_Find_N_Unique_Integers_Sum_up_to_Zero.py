from typing import List


# My First Solution:
class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n == 1:
            return [0]
        elif n % 2 == 0:
            return [x for x in range(n//2) for x in [-(x+1), x+1]] # +1 to avoid 0s when x = 0
        else:
            return [0]+[x for x in range((n-1) // 2) for x in [-(x + 1), x + 1]]

# ******* RESULTS ***********
# Runtime: 24 ms, faster than 97.62% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 59.33% of Python3 online submissions
