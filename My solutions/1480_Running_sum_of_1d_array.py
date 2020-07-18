class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        RSum = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            RSum.append(sum)
        return RSum