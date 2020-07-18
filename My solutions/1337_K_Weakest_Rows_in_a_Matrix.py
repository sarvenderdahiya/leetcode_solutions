from typing import List


# First Attempt
# class Solution:
#     def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
#         strength = [sum(x) for x in mat]
#         l = []
#         for i in range(k):
#             l.append(strength.index(min(strength)))
#             strength[strength.index(min(strength))] += 999
#         return l
#
# ***** RESULTS ****
# Runtime: 116 ms, faster than 64.45% of Python3 online submissions
# Memory Usage: 14.1 MB, less than 21.98% of Python3 online submissions


# Second attempt after learning Dictionary comprehension
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        strength = {i:sum(x) for i,x in enumerate(mat)}
        output = [item for item,val in sorted(strength.items(), key= lambda x:x[1])]
        return output[:k]

# ***** RESULTS ******
# Runtime: 116 ms, faster than 64.45% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 80.39% of Python3 online submissions



# TEST CASE
# mat = [[1,1,0,0,0],
#  [1,1,1,1,0],
#  [1,0,0,0,0],
#  [1,1,0,0,0],
#  [1,1,1,1,1]]
