from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return nums
        else:
            numcount = Counter(nums)
            mostcom = numcount.most_common(k)
            ans = [x[0] for x in mostcom]
            return ans