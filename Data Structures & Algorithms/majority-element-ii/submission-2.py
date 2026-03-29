class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return nums
        
        majority_element = []
        freq_map = {}
        limit = len(nums)//3
        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
                if freq_map[i] > limit:
                    if i not in majority_element:
                        majority_element.append(i)
            else:
                freq_map[i] = 1

        return majority_element
        

