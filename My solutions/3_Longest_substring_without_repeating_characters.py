class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        ans = 0
        start = 0
        temp = 0
        for idx, i in enumerate(s):
            if i not in seen:
                seen[i] = idx
                temp += 1
                # print(i ,idx,'tmp=' , temp)
                if ans < temp:
                    ans = temp
            else:
                if seen[i] < start:
                    temp += 1
                    # print(i, idx,'tmp=' , temp)
                    if ans < temp:
                        ans = temp
                    seen[i] = idx
                else:
                    temp = idx - seen[i]
                    start = seen[i]
                    seen[i] = idx
        return ans
