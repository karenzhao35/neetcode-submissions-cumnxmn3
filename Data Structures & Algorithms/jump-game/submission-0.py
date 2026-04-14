class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for index, val in enumerate(nums):
            if reach < index: return False
            new_reach = index + val 
            reach = max(reach, new_reach)
        
        return True