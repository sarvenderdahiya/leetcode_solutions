class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        rsum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            rsum.append(sum)
        return rsum