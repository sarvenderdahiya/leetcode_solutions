# ***** My ORIGINAL SOLUTION *******
#
# class Solution:
#     def findNumbers(self, nums: List[int]) -> int:
#         c = 0
#         for num in nums:
#             x = 10
#             while(num//x > 0):
#                 if num//x < 10:
#                     c += 1
#                 x *= 100
#         return c

# Better Solution:
import math
from typing import List

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        for num in nums:
            if (int(math.log10(num) + 1) % 2) == 0:
                c += 1
        return c
o = Solution()
print('asdasd', o.findNumbers( [12, 123, 1234, 123, 15]))
