class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0 
        maximum = max(nums)
        summation = 0
        has_zero = False
        for i in range(maximum+1):
            total += i 
        for e in nums: 
            if e == 0: 
                has_zero = True
            summation += e
        res = abs(summation - total)
        if res == 0 and has_zero: 
            return maximum + 1
        else: 
            return res