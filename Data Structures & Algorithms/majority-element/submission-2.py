class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        count = 0
        for i in nums:
            if i == candidate and count >= 0:
                count += 1
            elif i != candidate and count >= 0:
                count -= 1
            else: 
                candidate = i
                count = 0
        
        return candidate