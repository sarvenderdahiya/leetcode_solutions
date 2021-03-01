class Solution:
    def firstUniqChar(self, s: str) -> int:
        occurred = {}
        for i in s:
            if i in occurred:
                occurred[i] += 1
            else:
                occurred[i] = 1

        for i in range(len(s)):
            if occurred[s[i]] == 1:
                return i
        return -1
