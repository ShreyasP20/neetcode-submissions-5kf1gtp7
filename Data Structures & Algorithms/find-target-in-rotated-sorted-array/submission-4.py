class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return -1
        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        l, r = 0, len(nums) - 1
        while l < r:
            k = (l+r)//2
            if nums[k] > nums[r]:
                l = k + 1
            else:
                r = k
        min_index = l

        if min_index == 0:
            l, r = 0, len(nums) - 1
        elif target <= nums[min_index - 1] and target >= nums[0]:
            l, r = 0, min_index - 1
        else:
            l, r = min_index, len(nums) - 1
        
        while l <= r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1 