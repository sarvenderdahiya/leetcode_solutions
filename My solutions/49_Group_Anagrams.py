from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for i in strs:
            x = str(sorted(i))
            anagrams[x].append(i)

        return anagrams.values()