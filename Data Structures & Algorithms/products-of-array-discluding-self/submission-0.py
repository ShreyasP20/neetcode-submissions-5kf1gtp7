class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_nums = []
        product = 1
        for i in range(len(nums)):
            product = 1 
            for j in range(len(nums)):
                if i!=j:
                    product *= nums[j]
            
            product_nums.append(product)
        
        return product_nums
                
