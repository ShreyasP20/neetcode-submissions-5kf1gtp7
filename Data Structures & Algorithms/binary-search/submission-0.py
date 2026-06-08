class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        u = n - 1

        while l <= u:
            mid = int((l + u)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                u = mid - 1 
            else:
                l = mid + 1
            
        return -1 