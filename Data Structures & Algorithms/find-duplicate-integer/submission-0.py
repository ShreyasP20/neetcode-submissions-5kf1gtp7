class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        new_nums = []
        for i in nums:
            if i not in new_nums:
                new_nums.append(i)
            else:
                return i
        
        return 0