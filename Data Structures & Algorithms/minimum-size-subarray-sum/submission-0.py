class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        temp_sum = 0
        l = 0
        r = 0
        while (l < len(nums)) and (r<len(nums)):
            temp_sum = sum(nums[l:r+1])
            # print("temp_sum:",temp_sum)
            if temp_sum >= target:
                min_length = min(min_length, len(nums[l:r+1]))
                # print("min_length:",min_length)

            if temp_sum <= target and r < len(nums) - 1:
                r+= 1
            else:
                l+=1
        
        if min_length == float('inf'):
            return 0    
        return min_length
            

