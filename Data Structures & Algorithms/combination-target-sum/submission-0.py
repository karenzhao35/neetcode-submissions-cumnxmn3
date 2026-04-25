class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def dfs(i, arr, sumSoFar):
            if sumSoFar == target: result.append(arr)
            if sumSoFar > target: return 
            for q in range(i,len(nums)):
                dfs(q, arr+[nums[q]], sumSoFar+nums[q])
        for i in range(len(nums)):
            dfs(i, [nums[i]], nums[i])
        
        return result