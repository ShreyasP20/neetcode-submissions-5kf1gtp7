class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_nums = {}

        for i in nums:
            if i in majority_nums.keys():
                majority_nums[i] += 1
                # print(" Updated Key:",i," value:",majority_nums[i])
            else:
                majority_nums[i] = 1
                # print(" Created Key:",i," value:",majority_nums[i])

        majority_element = 0
        majority_count = 0
        for i in majority_nums.keys():
            if majority_nums[i] > majority_count:
                majority_count = majority_nums[i]
                majority_element = i


        return majority_element