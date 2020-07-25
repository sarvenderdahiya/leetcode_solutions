from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        out = []
        arr1.sort()
        for i in range(len(arr2)):
            pos1 = -1
            pos2 = -1
            lo = 0
            hi = len(arr1) - 1

            # To find first occurrence of arr2[i] in arr1
            while lo <= hi:
                mid = (hi+lo)//2
                if arr1[mid] < arr2[i]:
                    lo = mid + 1
                elif arr1[mid] == arr2[i]:
                    pos1 = mid
                    print("pos1 of ",arr2[i]," ",pos1 )
                    hi = mid - 1
                else:
                    hi = mid - 1

            # To find last occurrence of arr2[i] in arr1
            lo = 0
            hi = len(arr1) - 1
            while lo <= hi:
                mid = (hi+lo)//2
                if arr1[mid] < arr2[i]:
                    lo = mid + 1
                elif arr1[mid] == arr2[i]:
                    pos2 = mid
                    print("pos2 of ",arr2[i]," ",pos2 )
                    lo = mid + 1
                else:
                    hi = mid - 1

            # now add all those elements between pos1 and pos2 to output
            for i in range (pos1, pos2+1):
                out.append(arr1[i])
        diff = []
        for i in range(len(arr1)):
            if arr1[i] not in arr2:
                diff.append(arr1[i])
        print(sorted(diff))
        return out + (sorted(diff))


# Just to test the output with a test case
o = Solution()
print(o.relativeSortArray([2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31],[2,42,38,0,43,21]))

# Runtime: 48 ms, faster than 47.38% of Python3 online submissions
# Memory Usage: 13.9 MB, less than 67.01% of Python3 online submissions
