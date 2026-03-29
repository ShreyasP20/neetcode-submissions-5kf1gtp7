class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        j = len(nums)-1
        n = len(nums)
        num_swaps = 0
        
        for i in range(len(nums)):
            if nums[i] == val:
                num_swaps += 1
        
        i=0

        while i < j:
            while nums[i] != val and i < j:
                i += 1
            
            while nums[j] == val and i < j:
                j -= 1
            
            if i >= j: break

            nums[i], nums[j] = nums[j], nums[i]
        

        
        return n - num_swaps