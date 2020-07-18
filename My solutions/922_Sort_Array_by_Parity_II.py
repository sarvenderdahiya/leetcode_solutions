from typing import  List

# FIRST ATTEMPT   , see below for final attempt
#
# class Solution:
#     def sortArrayByParityII(self, A: List[int]) -> List[int]:
#         l = [0] * len(A)
#         pos = 0
#
#         for i in range (0,len(A), 2):
#             while pos < len(A):
#                 if A[pos] % 2 == 0:
#                     l[i] = A[pos]
#                     pos += 1
#                     break
#                 pos += 1
#
#         pos = 0
#         for i in range (1,len(A), 2):
#             while pos < len(A):
#                 if A[pos] % 2 != 0:
#                     l[i] = A[pos]
#                     pos += 1
#                     break
#                 pos += 1
#
#         return l
#
# ***** RESULTS ********
# Runtime: 256 ms, faster than 40.66% of Python3 online submissions
# Memory Usage: 16.5 MB, less than 23.13% of Python3 online submissions


# Second Attempt
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        l = [0] * len(A)
        od = 1
        ev = 0
        for elem in A:
            if elem % 2 == 0:
                l[ev] = elem
                ev += 2
            else:
                l[od] = elem
                od += 2
        return l

# ***** RESULTS *****
# Runtime: 212 ms, faster than 95.63% of Python3 online submissions
# Memory Usage: 16.4 MB, less than 33.08% of Python3 online submissions
