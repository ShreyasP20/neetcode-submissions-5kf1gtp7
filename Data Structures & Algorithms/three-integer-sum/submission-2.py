class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        threeSum_result = []
        for i,v in enumerate(nums):
            if nums[i] > 0:
                break
            
            elif i > 0 and nums[i] == nums[i-1]:
                continue

            j, k = i+1, len(nums)-1
            while j < k:
                temp_sum = nums[i] + nums[j] + nums[k]
                if  temp_sum == 0:
                    threeSum_result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif temp_sum < 0:
                    j += 1
                else:
                    k -= 1
        return threeSum_result