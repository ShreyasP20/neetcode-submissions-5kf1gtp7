class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        temp_sum = 0
        l = 0
        r = 0

        for r in range(len(nums)):
            temp_sum += nums[r]
            
            while temp_sum >= target:
                min_length = min(min_length, len(nums[l:r+1]))
                temp_sum -= nums[l]
                l += 1

        
        if min_length == float('inf'):
            return 0    
        return min_length
            

