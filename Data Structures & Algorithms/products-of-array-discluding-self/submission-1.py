class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1] * (len(nums)+1), [1] * (len(nums)+1)
        for i, num in enumerate(nums):
            left[i+1] = left[i] * num
        for i in range(len(nums)-1,-1,-1):
            num = nums[i]
            right[i] = right[i+1] * num 
        result = []
        for i, num in enumerate(nums):
            result.append(left[i] * right[i+1])
        return result