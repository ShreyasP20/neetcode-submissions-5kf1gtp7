class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        solution = []
        n = len(nums)
        def backtrack(i, cur_sum):
            if cur_sum == target:
                result.append(solution.copy())
                return
            
            if cur_sum>target or i == n:
                return
            
            solution.append(nums[i])
            backtrack(i, cur_sum+nums[i])
            solution.pop()
            backtrack(i+1, cur_sum)

            
        backtrack(0,0)

        return result