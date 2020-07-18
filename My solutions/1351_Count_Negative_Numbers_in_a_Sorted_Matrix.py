from typing import List

# MY final Solution:
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)):
            if grid[i][0] < 0:
                count += ((len(grid) - i) * len(grid[0]))
                break
            for j in range(1,len(grid[0])):
                if grid[i][j] < 0:
                    count += (len(grid[0])-j)
                    break
        return count

# ******* RESULTS ********
# Runtime: 124 ms, faster than 88.93% of Python3 online submissions.
# Memory Usage: 14.7 MB, less than 67.55% of Python3 online submissions.

# Just to test a testcase
o = Solution()
print(o.countNegatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))