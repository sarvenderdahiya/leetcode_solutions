from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        conflict = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                conflict += 1
                if conflict > 1:
                    return False
                if (i+2) <= len(nums)-1:
                    if (nums[i+2] < nums[i]) and (i != 0):
                        if nums[i-1] > nums[i+1]:
                            return False
        return True

# Runtime: 204 ms, faster than 66.22% of Python3 online submissions
# Memory Usage: 15 MB, less than 61.60% of Python3 online submissions


# Thing to Learn:
# two possibilities

# eg:[1,*4*,*2*,3]  ==> [1,2,2,3]
# if i < 1 or nums[i - 1] <= nums[i + 1]:
#     nums[i] = nums[i + 1]
# eg:[2,3,*3*,*2*,4] ==> [2,3,3,3,4]
#  else:
#                     nums[i+1] = nums[i]

o = Solution()
print(o.checkPossibility([3,4,2,3]))