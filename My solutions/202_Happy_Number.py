class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        seen.add(n)
        squares = [i*i for i in range(10)]
        while True:
            if n == 1:
                return True
            sum = 0
            while n > 0:
                sum += squares [n%10]
                n = n//10
            n = sum
            if n in seen:
                return False
            else:
                seen.add(n)