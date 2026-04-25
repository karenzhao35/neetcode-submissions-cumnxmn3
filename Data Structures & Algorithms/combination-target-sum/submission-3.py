class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        nums.sort()
        def dfs(i, sumSoFar):
            if sumSoFar == target: result.append(path.copy())
            for q in range(i,len(nums)):
                if sumSoFar+nums[q] <= target:
                    path.append(nums[q])
                    dfs(q, sumSoFar+nums[q])
                    path.pop()
                else: return
        # for i in range(len(nums)):
        #     path.append(nums[i])
        #     dfs(i, nums[i])
        #     path.pop()
        dfs(0,0)
        return result