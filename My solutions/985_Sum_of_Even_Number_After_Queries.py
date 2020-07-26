from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        sumeven = sum([x for x in A if x % 2 == 0])

        for q in queries:
            val, idx = tuple(q)
            if A[idx] % 2 == 0:
                if val % 2 == 0:
                    sumeven += val
                else:
                    sumeven -= A[idx]

            else:
                if val % 2 == 1:
                    sumeven += (A[idx] + val)

            A[idx] += val
            answer.append(sumeven)

        return answer

# Runtime: 556 ms, faster than 76.67% of Python3 online submissions
# Memory Usage: 19.7 MB, less than 36.59% of Python3 online submissions
