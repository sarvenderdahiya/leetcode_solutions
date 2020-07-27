# Naiive SOLUTION FIRST APPROACH
# class Solution:
#     def addDigits(self, num: int) -> int:
#         while num > 9:
#             num = sum([int(x) for x in str(num)])
#         return num


# O(1) complexity Solution !!!!!!!!!!!!!!!!!
# class Solution:
#     def addDigits(self, num: int) -> int:
#         if num == 0:
#             return 0
#         elif num % 9 == 0:
#             return 9
#         else:
#             return num % 9
# Runtime: 32 ms, faster than 72.68% of Python3 online submissions
# Memory Usage: 14 MB, less than 16.45% of Python3 online submissions


# THE BEST OF ALL
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num-1) % 9 if num else 0


o = Solution()
print(o.addDigits(38))

# Runtime: 32 ms, faster than 90.22% of Python3 online submissions
# Memory Usage: 13.8 MB, less than 49.68% of Python3 online submissions