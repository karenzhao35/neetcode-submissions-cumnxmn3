class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)-1
        if n == 0: return nums[0]
        l, r = 0, n

        while l <= r: 
            m = l + ((r - l) // 2)
            print(m)
            if m == 0 and nums[0] < nums[n]: 
                return nums[0]
            elif m == n and nums[n] < nums[n-1]:
                return nums[n]
            elif nums[m] < nums[m-1]:
                return nums[m]
            elif nums[m] > nums[m+1]:
                return nums[m+1]
            
            if nums[m] > nums[l] and nums[m] > nums[r]:
                l = m + 1
            else: 
                r = m - 1 
        return -1
