class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        N = len(nums)

        def dfs(i, cur):
            self.result.append(cur.copy())
            if i == N: 
                return 

            for j in range(i+1, N):

                cur.append(nums[j])
                dfs(j, cur)
                cur.pop()

        dfs(-1,[])
        return self.result