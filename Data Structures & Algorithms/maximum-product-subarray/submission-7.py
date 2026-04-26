class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m = -11
        p = 1
        for i in range(len(nums)):
            p = nums[i]
            m = max(p, m)
            for j in range(i+1, len(nums)):
                p *= nums[j]
                m = max(p, m)

        return m


        