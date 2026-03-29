class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product_nums = [0] * n

        left_product = 1
        for i,x in enumerate(nums):
            product_nums[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        for i in range(n-1, -1, -1):
            product_nums[i] *= right_product
            right_product *= nums[i]
        
        return product_nums
        
                
