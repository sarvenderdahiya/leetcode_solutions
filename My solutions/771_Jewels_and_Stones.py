from collections import Counter

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        st = Counter(stones)
        ans = 0
        for j in jewels:
            ans += st[j]
        return ans