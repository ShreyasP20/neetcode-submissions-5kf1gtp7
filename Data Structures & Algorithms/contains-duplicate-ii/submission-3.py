class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        has_nums = dict()
        for i in range(len(nums)):
            if nums[i] not in has_nums.keys():
                has_nums[nums[i]] = i
            else:
                print(has_nums)
                diff = abs(has_nums[nums[i]] - i)
                print(diff)
                if  diff <= k:
                    return True
                has_nums[nums[i]] = i
        
        return False