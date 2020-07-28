from typing import List


# Time Limit Exceeded In this Solution O(n^4)  .... or O(mn^3) if m > n ... or O (m^3 n) if m < n
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         squares = sum([sum(x) for x in matrix]) #individual 1s
#         i, n = 0, 1
#         while (i + n) <= (len(matrix) - 1):
#             j = 0
#             if (j + n) > (len(matrix[0]) - 1):
#                 break
#             while (j + n) <= (len(matrix[0]) - 1):
#                 impure = 0
#                 for x in range(n+1):
#                     for z in range(n+1):
#                         if matrix[i + x][j + z] != 1:
#                             impure += 1
#                             break
#                     if impure == 1:
#                         break
#                 if impure == 0:
#                     squares += 1
#                     # print ("square found beginning at ",i,j,"of length",n )
#                 j += 1
#
#             i += 1
#             if (i+n) > (len(matrix)-1):
#                 i = 0
#                 n += 1
#
#         return squares
# Time Limit Exceeded


# ********* THIS SOLUTION NEEDS HELP WITH CALCULATION of COMPLEXITY **************
# Is this a O(m*n^2) Solution ?
#
# class Solution:
#     def countSquares(self, matrix: List[List[int]]) -> int:
#         squares = 0
#         row, col, size = 0, 0, 0
#         while row < len(matrix):
#             impure = 0
#             if (row + size) < len(matrix) and (col + size) < len(matrix[0]):
#                 for p in range(size + 1):
#                     if matrix[row + p][col + size] != 1:
#                         impure += 1
#                         #print("impurity at ", row+p, col+size)
#                         break
#                     if matrix[row + size][col + p] != 1:
#                         impure += 1
#                         #print("impurity at ", row+size, col+p)
#                         break
#                 if impure:
#                     col += 1
#                     if col > len(matrix[0]) - 1:
#                         row += 1
#                         col = 0
#                     size = 0
#                     continue
#
#                 else:
#                     #print("square found at", row, col, "of size", size)
#                     squares += 1
#                     size += 1
#
#             else:
#                 col += 1
#                 if col > len(matrix[0]) - 1:
#                     row += 1
#                     col = 0
#                 size = 0
#
#         return squares

# Runtime: 984 ms, faster than 19.29% of Python3 online submissions
# Memory Usage: 15.9 MB, less than 80.41% of Python3 online submissions


# Dynamic Programming Solution O(m*n)
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0

        rows = len(matrix)
        cols = len(matrix[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 1:
                    if r == 0 or c == 0:
                        result += 1
                        print("fount 1  at ", r, c, "of size 1")
                    else:
                        curr = min(matrix[r - 1][c - 1], matrix[r][c - 1], matrix[r - 1][c]) + matrix[r][c]
                        result += curr
                        print("fount", curr, " at ", r, c, "of largest size", curr)
                        matrix[r][c] = curr
        return result



# TEST CASE
o = Solution()
print(o.countSquares([[0,1,1,1],[1,1,1,1],[0,1,1,1]]))
# Expected answer 15
