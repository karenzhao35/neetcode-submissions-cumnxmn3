class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_arr, max_arr = [0] * len(nums), [0] * len(nums)
        min_arr[0], max_arr[0] = nums[0], nums[0]
        

        for i in range(1, len(nums)):
            if nums[i] > 0: 
                min_arr[i] = min(min_arr[i-1]*nums[i], nums[i])
                max_arr[i] = max(max_arr[i-1]*nums[i], nums[i])
            elif nums[i] < 0:
                min_arr[i] = min(max_arr[i-1]*nums[i], nums[i])
                max_arr[i] = max(min_arr[i-1]*nums[i], nums[i])
        print(min_arr, max_arr)
        return max(max_arr)