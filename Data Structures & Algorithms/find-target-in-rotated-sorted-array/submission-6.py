class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1
        n = len(nums)

        while low <= high:
            med = (low + high)//2
            if nums[med] == target: return med
            ls, rs = (med-1)%n, (med+1)%n
            if nums[ls] == target: return ls
            if nums[rs] == target: return rs
            if nums[high] == target: return high
            if nums[low] == target: return low

            if target > nums[med] and nums[high] >= target:
                low=med+1
            elif target < nums[med] and nums[low] <= target:
                high= med-1
            elif nums[low] > nums[high] and target < nums[low]:
                low = med+1
            else:
                high = med-1
        return -1