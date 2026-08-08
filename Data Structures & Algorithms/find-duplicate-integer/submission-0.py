class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set(nums)
        return ( sum(nums) - sum(s) ) // (len(nums) - len(s))